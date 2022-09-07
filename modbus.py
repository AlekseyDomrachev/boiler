from pyModbusTCP.server import ModbusServer
from threading import Thread
import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
server = ModbusServer(ip, 502, no_block=True)
MB_DATA = 0
MB_READ_DATA = 0
DATA_SIZE = 32000

print('Starting server...')
server.start()
if server.is_run:
    print('Server is online at:', ip)


class Read(Thread):
    def __init__(self):
        super(Read, self).__init__()
        self.read_complete = False
        self.data_old = 0
        self.data = 0

    def run(self):
        while server.is_run:
            if self.data_old != server.data_bank.get_holding_registers(0, DATA_SIZE):
                self.data_old = server.data_bank.get_holding_registers(0, DATA_SIZE)
                self.read_complete = True
            if self.read_complete:
                self.data = server.data_bank.get_holding_registers(0, DATA_SIZE)
                self.read_complete = False
            time.sleep(0.1)


class Write(Thread):
    def __init__(self, data_old, data):
        super(Write, self).__init__()
        self.data_old = data_old
        self.data = data

    def run(self):
        while server.is_run:
            if self.data != self.data_old and type(self.data_old) is list and type(self.data) is list:
                counter = 0
                for data_to_send in self.data:
                    if data_to_send != self.data_old[counter]:
                        server.data_bank.set_holding_registers(counter, [data_to_send])
                    counter += 1