from tentnenTEE import *
from space_war_BUT_TENET import *
from random import randint
j = 0
while True:
    alphabets = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    red_size = randint(1, 25)
    blue_size = randint(1, 25)
    blue, red = 'BBAAABBAAABB', 'AAA'
    # for i in range(red_size):
    #     red += str(alphabets[randint(0, 25)])
    # for i in range(blue_size):
    #     blue += str(alphabets[randint(0, 25)])

    POOM = space_war_BUT_TENET(red, blue)
    TEE = tentnetTEE(red, blue)

    if POOM != TEE:
        print('Input : ', red, blue)
        print('PooM',POOM)
        print('Tee',TEE)
        break
    else:
        j += 1
        print(f'Testcase {j} Correct')
        print('PooM',POOM)
        print('Tee',TEE)
    break