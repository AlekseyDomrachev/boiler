from pyModbusTCP.server import ModbusServer
from threading import Thread
import time
# import copy
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
# ip = '192.168.1.105'
server = ModbusServer(ip, 502, no_block=True)
MB_DATA = []
MB_DATA_OLD = 0
data_size = 32#000
while len(MB_DATA) < data_size:
    MB_DATA.append(0)

print('Starting server...')
server.start()
if server.is_run:
    print('Server is online at:', ip)


class Mb(Thread):
    def __init__(self, data, period=0.1):
        super(Mb, self).__init__()
        self.period = period
        self.data = data
        self.value = 0
        # self.read_complit = False
        # self.data_old = 0
        # self.value_old = 0

    def run(self):
        while True:
            if server.is_run:
                if self.value != server.data_bank.get_holding_registers(0, data_size):
                    self.value = server.data_bank.get_holding_registers(0, data_size)
                    # self.read_complit = True
                    # self.value_old = list(self.value)
                # print(self.data, self.value)
                if self.data != self.value:
                    # print('setting modbus done!')
                    print(self.data)
                    server.data_bank.set_holding_registers(0, self.data)
                    # self.data_old = list(self.data)
            time.sleep(self.period)