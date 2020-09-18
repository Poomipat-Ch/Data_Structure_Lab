def asteroid_collision(asts):
    if len(asts) < 2:
        return asts
    
    tmp = asteroid_collision(asts[1:])

    if len(tmp) != 0 and asts[0] > 0 and tmp[0] < 0:
        if asts[0] > abs(tmp[0]):
            return asteroid_collision([asts[0]]+tmp[1:])
        elif asts[0] == abs(tmp[0]):
            return tmp[1:] if len(tmp) > 1 else []
        else:
            return tmp
    else:
        return [asts[0]]+ tmp
x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))