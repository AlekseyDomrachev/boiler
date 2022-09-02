from pyModbusTCP.server import ModbusServer
from threading import Thread
import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
# ip = '192.168.1.105'
server = ModbusServer(ip, 502, no_block=True)
MB_DATA = []
MB_DATA_OLD = 0
MB_COMPLEAT = False
data_size = 32000
while len(MB_DATA) < data_size:
    MB_DATA.append(0)

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
            time.sleep(self.period)


class Write(Thread):
    def __init__(self, data, period=0.1):
        super(Write, self).__init__()
        self.period = period
        self.data = data
        # self.value = 0
        # self.read_complit = False
        self.data_old = 0
        # self.value_old = 0

    def run(self):
        while True:
            if server.is_run:
                # if self.data != self.data_old:
                server.data_bank.set_holding_registers(0, self.data)
                # self.data_old = self.data
            time.sleep(self.period)