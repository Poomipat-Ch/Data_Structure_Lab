
n,lst = input('Enter Input : ').split('/')
lst = list(map(int, lst.split()))

if len(lst) != int(n)//2 + 1 or int(n) % 2 == 0:
    print('Incorrect Input')
else:
    total = 0
    tmp = []
    if len(lst) % 2 != 0:
        tmp.append(lst.pop(-1))
    while lst or tmp:
        if len(lst) > 1:
            a,b = lst.pop(-1), lst.pop(-1)
            x = min(a,b)
            tmp.append(x)
            total += a-x + b-x 
        elif len(tmp) > 1:
            a,b = tmp.pop(-1), tmp.pop(-1)
            lst.append(a if a>b else b)
            lst.append(b if a>b else a)
        elif tmp:
            total += tmp.pop()
        else:
            break
    print(total)

