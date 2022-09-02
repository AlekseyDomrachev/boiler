from modbus import *


# mbr = Read()
# mbr.start()
# mbw = Write(MB_DATA)
# mbw.start()
r = 0
t1 = 0
t2 = 0
r1 = 0
# while True:
    #Читать нужно, когда данные готовы
    # Определим время записи MB

# t1 = time.time()
# server.data_bank.set_holding_registers(0, MB_DATA)
# t2 = time.time()
# print(t1)
# print(t2)
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
        # MB_DATA[2] += 1

    # t2 = time.time()
    # print(t2-t1, r1)
    # MB_DATA[2] += 1
    # print(MB_DATA)
    # MB_DATA[2] = 1
    if MB_DATA != MB_DATA_OLD:
        counter = 0
        for data_to_send in MB_DATA:
            if data_to_send != MB_DATA_OLD[counter]:
                server.data_bank.set_holding_registers(counter, [data_to_send])
            counter += 1
        # print(MB_DATA, MB_DATA_OLD)
        # MB_DATA_OLD = MB_DATA
        # mbw.data = MB_DATA
        # server.data_bank.set_holding_registers(0, MB_DATA)







# print(t2)

    # if MB_DATA != server.data_bank.get_holding_registers(0, data_size):
    #     MB_DATA = server.data_bank.get_holding_registers(0, data_size)
    #     print('read_compleate', r)
    #     r += 1
    # if mbr.read_complit:
    #     MB_DATA = mbr.value
    #     mb1.read_complit = False
    #     print(MB_DATA[0])
    # if not mb1.is_alive():
    # MB_DATA = copy.deepcopy(mb1.value)
    # print(id(MB_DATA), id(mb1.data))
    # print(MB_DATA)
        # mb1.start()
    # mb1.join(0.1)
    # if MB_DATA[0] == 1:
    #     MB_DATA[2] += 1
    # if mb1.value[0] == 1:
    # print(MB_DATA)
    #     MB_DATA[1] = 55
    # else:
    #     MB_DATA[1] = 0
    # MB_DATA[2] += 1
    # print(MB_DATA, mb1.value)
        # print(MB_DATA[0], MB_DATA[2])
        # print()
    # print(id(MB_DATA), id(mb1.value))
    # print(MB_DATA, mb1.value)

    # print(MB_DATA[0], MB_DATA[2])
    # print(mb1.value)
    # time.sleep(0.1)

    # if MB_DATA != MB_DATA_OLD:
    #     mb1.data = list(MB_DATA)
    # print(id(mb1.data), id(MB_DATA), id(mb1.value))
    # mbw.data = MB_DATA
    # r += 1
    # if M/TA_OLD = list(MB_DATA)
    # print(MB_DATA)

    # r += 1