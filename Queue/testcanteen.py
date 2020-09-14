from canteenTEE import *
from Canteen import *
from random import randint

if __name__ == "__main__":
    TOKEN = "DE"
    i = 0

    while True:
        size_left = randint(1, 10)
        size_right = randint(1, 10)
        left_for_right = []
        left = ''
        right = ''
        for i in range(size_left):
            x = str(randint(1,3))
            left += x+' '
            x += '0'+str(randint(0,4))
            left_for_right.append(x)
            left += x+',' if i < size_left-1 else x
        for i in range(size_right):
            x = TOKEN[randint(0,1)]
            if x == 'E':
                x += ' '+left_for_right[randint(0,len(left_for_right)-1)]
                x += ',' if i < size_right-1 else ''
                right += x
            else:
                x += ',' if i < size_right-1 else ''
                right += x
        print(left+'/'+ right)
        TEE = canteenTEE([left,right])
        PooM = canteenPooM([left, right])

        if TEE == PooM:
            i += 1
            print(f'case {i} : ถูกต้อง')
        else:
            print('\n------------Wrong---------------\nPoom : '+PooM)
            print('Tee : '+TEE)
            break