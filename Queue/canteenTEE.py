


def canteenTEE(inp):
    # inp = input('Enter Input : ').split('/')
    right = []
    final = []
    result = ''

    for i in inp[1].split(','):
        right.append(i.split())
    lst = dict()
    for data in inp[0].split(','):
        data = data.split()
        lst[data[1]] = lst.get(data[1], data[0])

    for i in range(len(right)):
        check = 1
        if right[i][0] == 'E' and len(final) == 0:
            final.append(right[i][1])
        elif right[i][0] == 'E':
            for j in range(len(final)):
                if lst[right[i][1]] == lst[final[j]]:
                    final.insert(j+1, right[i][1])
                    check = 0
                    break
            if check == 1:
                final.append(right[i][1])

        elif right[i][0] == 'D':
            if len(final) == 0:
                result +=' Empty'
            else:
                result += ' '+final.pop(0)
    return result