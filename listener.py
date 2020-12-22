# sudo socat -d -d pty,raw,echo=0,link=/dev/ttyS20 pty,raw,echo=0,link=/dev/ttyS21
import test_pb2
import time
import serial
import psutil
import json
import os
import math
import threading
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as mticker
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline


class Listener:
    def __init__(self, port):
        self.received_message = test_pb2.TEST_MSG()
        self.port = port
        self.serial_port = serial.Serial(self.port, 9600)
        self.received_data = ""
        self.cpus_usage_data = [[] for i in range(4)]
        self.free_memory_data = []
        self.used_memory_data = []
        self.new_data_available = False

    def _get_data(self):
        data = self.serial_port.read_all()
        if data:
            self.received_message.ParseFromString(data)
            self.received_data = {
                'timestamp': self.received_message.timestamp,
                'num_cpu_cores': self.received_message.num_cpu_cores,
                'cpu_usage_per_core': [x for x in self.received_message.cpu_usage_per_core.split(" ")],
                'total_memory': self.received_message.total_memory,
                'free_memory': self.received_message.free_memory,
                'available_memory': self.received_message.available_memory,
                'memory_used': self.received_message.memory_used,
            }
            self.new_data_available = True

    def _plot_for_cpus(self):
        if self.cpus_usage_data:
            cpu1, cpu2, cpu3, cpu4 = self.cpus_usage_data
            ax1.clear()
            ax1.yaxis.tick_right()
            ax1.set_title("CPU History")
            ax1.set_xlim([max(0, len(cpu1) - 30), len(cpu1) + 30])
            ax1.set_ylim([0, 110])
            ax1.set_xlabel('time [s]')
            ax1.set_ylabel('usage [%]')
            ax1.yaxis.set_label_position("right")

            # smooth plot line - this works, but I don't like the look
            # try:
            #     # for cpu1
            #     cpu1_new_x = np.linspace(np.array(range(len(cpu1))).min(),
            #                              np.array(range(len(cpu1))).max(),
            #                              200)
            #     cpu1_BSpline = make_interp_spline(range(len(cpu1)), cpu1)
            #     cpu1_new_y = cpu1_BSpline(cpu1_new_x)

            #     # for cpu2
            #     cpu2_new_x = np.linspace(np.array(range(len(cpu2))).min(),
            #                              np.array(range(len(cpu2))).max(),
            #                              200)
            #     cpu2_BSpline = make_interp_spline(range(len(cpu2)), cpu2)
            #     cpu2_new_y = cpu2_BSpline(cpu2_new_x)

            #     # for cpu3
            #     cpu3_new_x = np.linspace(np.array(range(len(cpu3))).min(),
            #                              np.array(range(len(cpu3))).max(),
            #                              200)
            #     cpu3_BSpline = make_interp_spline(range(len(cpu3)), cpu3)
            #     cpu3_new_y = cpu3_BSpline(cpu3_new_x)

            #     # for cpu4
            #     cpu4_new_x = np.linspace(np.array(range(len(cpu4))).min(),
            #                              np.array(range(len(cpu4))).max(),
            #                              200)
            #     cpu4_BSpline = make_interp_spline(range(len(cpu4)), cpu4)
            #     cpu4_new_y = cpu4_BSpline(cpu4_new_x)
            # except ValueError:
            #     return

            # store labels for each plot
            cpu1_label, = ax1.plot(range(len(cpu1)), cpu1, 'g')
            cpu2_label, = ax1.plot(range(len(cpu2)), cpu2, 'y')
            cpu3_label, = ax1.plot(range(len(cpu3)), cpu3, 'm')
            cpu4_label, = ax1.plot(range(len(cpu4)), cpu4, 'b')

            # store labels description
            cpu1_label_text = f'CPU1 {cpu1[-1]}%'
            cpu2_label_text = f'CPU2 {cpu2[-1]}%'
            cpu3_label_text = f'CPU3 {cpu3[-1]}%'
            cpu4_label_text = f'CPU4 {cpu4[-1]}%'

            # create legend
            ax1.legend([cpu1_label, cpu2_label, cpu3_label, cpu4_label],
                       [cpu1_label_text, cpu2_label_text,
                        cpu3_label_text, cpu4_label_text],
                       loc='center',
                       bbox_to_anchor=(0.5, -0.2),
                       ncol=4)

    def _plot_for_memory(self, free_memory, total_memory, used_memory):
        ax2.clear()
        ax2.yaxis.tick_right()
        ax2.set_title("Memory Info")
        ax2.set_xlabel('time [s]')
        ax2.set_ylabel('usage [%]')
        ax2.yaxis.set_label_position("right")
        ax2.set_xlim(
            [max(0, len(self.used_memory_data) - 30), len(self.used_memory_data) + 30])
        ax2.set_ylim([0, 110])

        # store labels for each plot
        free_label, = ax2.plot(
            range(len(self.free_memory_data)), self.free_memory_data, 'g')
        used_label, = ax2.plot(
            range(len(self.used_memory_data)), self.used_memory_data, 'y')

        # store labels description
        free_label_text = f'Free: {float(free_memory) / 1000000000:.2f}GiB ({self.free_memory_data[-1]:.2f}%) out of {float(total_memory) / 1000000000:.2f}GiB'
        used_label_text = f'Used: {float(used_memory) / 1000000000:.2f}GiB ({self.used_memory_data[-1]:.2f}%) out of {float(total_memory) / 1000000000:.2f}GiB'

        # create legend
        ax2.legend([free_label, used_label],
                   [free_label_text, used_label_text],
                   loc='center',
                   bbox_to_anchor=(0.5, -0.2),
                   ncol=1)

    def animation(self, i):
        # get data
        if self.received_data:
            if cpus_usage_list := self.received_data.get('cpu_usage_per_core', None):
                for plot_data, new_data in zip(self.cpus_usage_data, cpus_usage_list):
                    plot_data.append(float(new_data))

            if (total_memory := self.received_data.get('total_memory', None)) and (free_memory := self.received_data.get('free_memory', None)) and (used_memory := self.received_data.get('memory_used', None)) and (available_memory := self.received_data.get('available_memory', None)):
                use_mem_pr = float(
                    int(total_memory) - int(available_memory)) / float(total_memory) * 100
                free_mem_pr = float(free_memory) / float(total_memory) * 100
                self.free_memory_data.append(free_mem_pr)
                self.used_memory_data.append(use_mem_pr)

            # draw plots
            self._plot_for_cpus()
            self._plot_for_memory(free_memory, total_memory, used_memory)

    def _save_to_file(self):
        with open("results.json", "a") as f:
            if self.new_data_available:
                json.dump(self.received_data, f)
                f.write("\n")
                self.new_data_available = False

    def listen(self):
        while True:
            # read data
            self._get_data()

            # store data
            self._save_to_file()


if __name__ == "__main__":
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(20, 10))
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)

    listener = Listener("/dev/ttyS21")
    x = threading.Thread(target=listener.listen, daemon=True)
    x.start()

    ani = animation.FuncAnimation(fig, listener.animation, interval=500)
    plt.show()
