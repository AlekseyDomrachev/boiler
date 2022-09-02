from pyModbusTCP.server import ModbusServer
from threading import Thread
# import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
server = ModbusServer(ip, 502, no_block=True)
MB_DATA = 0
MB_READ_DATA = 0
MB_COMPLEAT = False
DATA_SIZE = 32000

# while len(MB_DATA) < data_size:
#     MB_DATA.append(0)

print('Starting server...')
server.start()
if server.is_run:
    print('Server is online at:', ip)


class Read(Thread):
    def __init__(self, period=0.1):
        super(Read, self).__init__()
        self.period = period
        self.read_complit = False
        self.value = 0

    def run(self):
        while True:
            if server.is_run:
                if self.value != server.data_bank.get_holding_registers(0, data_size):
                    self.value = server.data_bank.get_holding_registers(0, data_size)
                    self.read_complit = True
            # time.sleep(self.period)


class Write(Thread):
    def __init__(self, data_old, data):
        super(Write, self).__init__()
        # self.period = address
        self.data = data
        self.data_old = data_old
        # self.value = 0
        # self.read_complit = False
        # self.data_old = 0
        # self.value_old = 0

    def run(self):
        while True:
            if server.is_run:
                # print(self.data_old)
                # print(type(self.data_old))
                if self.data != self.data_old and type(self.data_old) is list and type(self.data) is list:
                    counter = 0
                    for data_to_send in self.data:
                        if data_to_send != self.data_old[counter]:
                            server.data_bank.set_holding_registers(counter, [data_to_send])
                        counter += 1
                # if self.data != self.data_old:
                # server.data_bank.set_holding_registers(0, self.data)
                # self.data_old = self.data
            # time.sleep(self.period)