# sudo socat -d -d pty,raw,echo=0,link=/dev/ttyS20 pty,raw,echo=0,link=/dev/ttyS21
import test_pb2
import time
import serial
import psutil


class Daemon:
    def __init__(self, port):
        self.message = test_pb2.TEST_MSG()
        self.port = port
        self.serial_port = serial.Serial(self.port, 9600)

    def _get_free_mem_info(self):
        return str(psutil.virtual_memory()._asdict()['free'])

    def _get_total_mem_info(self):
        return str(psutil.virtual_memory()._asdict()['total'])

    def _get_available_mem_info(self):
        return str(psutil.virtual_memory()._asdict()['available'])

    def _get_used_mem_info(self):
        return str(psutil.virtual_memory()._asdict()['used'])

    def _get_cpu_num_cores_info(self):
        return str(psutil.cpu_count(logical=True))

    def _get_cpu_usage_info(self):
        return ' '.join(str(cpu_usage) for cpu_usage in psutil.cpu_percent(interval=2, percpu=True))

    def _create_message(self):
        self.message.timestamp = str(time.time())
        self.message.num_cpu_cores = self._get_cpu_num_cores_info()
        self.message.cpu_usage_per_core = self._get_cpu_usage_info()
        self.message.total_memory = self._get_total_mem_info()
        self.message.free_memory = self._get_free_mem_info()
        self.message.available_memory = self._get_available_mem_info()
        self.message.memory_used = self._get_used_mem_info()

    def _send_message(self):
        self.serial_port.write(self.message.SerializeToString())

    def _clear_message(self):
        self.message = test_pb2.TEST_MSG()

    def run(self):
        while True:
            # wait some time to not spam with messages
            # time.sleep(0.3)

            # crate message
            self._create_message()

            # send message
            self._send_message()

            # clear the message
            self._clear_message()


daemon = Daemon("/dev/ttyS20")
daemon.run()
