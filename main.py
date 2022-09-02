from modbus import *

# mbr = Read()
# mbr.start()
# mbw = Write(MB_DATA)
# mbw.start()
while True:
    t1 = time.time()
# MB_DATA = server.data_bank.get_holding_registers(0, data_size)# Это операция присвоения а не само чтение!!! и в случае изменения там в любой
#момент времени оно поменяется в любом месте программы!
#Нужно сделать так:
# MB_DATA = list(server.data_bank.get_holding_registers(0, data_size))
#А лучше всего так:
    if MB_DATA_OLD != server.data_bank.get_holding_registers(0, data_size):# Но в этом случае, при изменении в программе MB_DATA тут сработает и затрет!!!
        MB_DATA_OLD = server.data_bank.get_holding_registers(0, data_size)
        MB_COMPLEAT = True

    if MB_COMPLEAT:
        MB_DATA = server.data_bank.get_holding_registers(0, data_size)
        MB_COMPLEAT = False

    if MB_DATA[0] == 1:
        qw = 0
        for q in MB_DATA:
            if qw != 0:
                MB_DATA[qw] +=1
            qw += 1

    if MB_DATA != MB_DATA_OLD:
        counter = 0
        for data_to_send in MB_DATA:
            if data_to_send != MB_DATA_OLD[counter]:
                server.data_bank.set_holding_registers(counter, [data_to_send])
            counter += 1