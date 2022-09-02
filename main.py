from modbus import *
import copy

mb1 = Mb(MB_DATA)
mb1.start()
r = 0
while True:
    #Читать нужно, когда данные готовы
    # if mb1.read_complit:
    MB_DATA = list(mb1.value)
    #     mb1.read_complit = False
    #     print(MB_DATA[0])
    # if not mb1.is_alive():
    # MB_DATA = copy.deepcopy(mb1.value)
    # print(id(MB_DATA), id(mb1.data))
    # print(MB_DATA)
        # mb1.start()
    # mb1.join(0.1)
    if MB_DATA[0] == 1:
        MB_DATA[2] += 1
    # if mb1.value[0] == 1:
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
    time.sleep(1)

    # if MB_DATA != MB_DATA_OLD:
    #     mb1.data = list(MB_DATA)
    # print(id(mb1.data), id(MB_DATA), id(mb1.value))
    # r += 1