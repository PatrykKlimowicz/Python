# sudo socat -d -d pty,raw,echo=0,link=/dev/ttyS20 pty,raw,echo=0,link=/dev/ttyS21
import test_pb2, time, serial, psutil, json, os

class Listener:
    def __init__(self, port):
        self.received_message = test_pb2.TEST_MSG()
        self.port = port
        self.serial_port = serial.Serial(self.port, 9600)
        self.received_data = ""

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

    def _save_to_file(self):
        with open("results.json", "a") as f:
            if self.received_data:
                json.dump(self.received_data, f)
                f.write("\n")

    def _print_data(self):
        if self.received_data:
            print(self.received_data)

    def _clear(self):
        self.message = test_pb2.TEST_MSG()
        self.received_data = ""


    def listen(self):
        while True:
            # read data
            self._get_data()

            # print data to the console
            self._print_data()

            # store data
            self._save_to_file()

            # clear state
            self._clear()

listener = Listener("/dev/ttyS21")
listener.listen()