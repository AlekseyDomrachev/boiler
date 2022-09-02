from modbus import *

# mbr = Read()
# mbr.start()
mbw = Write(MB_READ_DATA, MB_DATA)
mbw.start()

while True:
    if MB_READ_DATA != server.data_bank.get_holding_registers(0, DATA_SIZE):# Но в этом случае, при изменении в программе MB_DATA тут сработает и затрет!!!
        MB_READ_DATA = server.data_bank.get_holding_registers(0, DATA_SIZE)
        MB_COMPLEAT = True

    if MB_COMPLEAT:
        MB_DATA = server.data_bank.get_holding_registers(0, DATA_SIZE)
        MB_COMPLEAT = False



    if MB_DATA[0] == 1:
        MB_DATA[2] += 1





    if MB_DATA != MB_READ_DATA:
        mbw.data = MB_DATA
        mbw.data_old = MB_READ_DATA
