

def tentnetTEE(reds, blues):
    red = []
    blue = []
    defuse = []
    explosiveBlue = 0
    explosiveRed = 0
    mistake = 0

    for i in range(len(reds)):
        red.append(reds[i])
    for i in range(len(blues)):
        blue.append(blues[i])
    i = 0
    while i in range(len(blue)):
        if i < len(blue) - 2 and blue[i] == blue[i+1] == blue[i+2]:
            defuse.append(blue[i])
            del blue[i:i+3]
            explosiveBlue += 1
            i = 0
        else:
            i += 1
    freeze = len(blue)
    x = len(defuse)
    i = 0

    while i in range(len(red)):
        if i < len(red) - 2 and red[i] == red[i+1] == red[i+2] and len(defuse) > 0:
            if red[i] == defuse[x-1]:
                del red[i:i+2]
                mistake += 1
                i = 0
                defuse.pop(x-1)
                x -= 1
            else:
                red.insert(i+2, defuse[x-1])
                defuse.pop(x-1)
                i = 0
                x -= 1

        elif i < len(red) - 2 and red[i] == red[i+1] == red[i+2] and len(defuse) == 0:
            del red[i:i+3]
            explosiveRed += 1
            i = 0
        else:
            i += 1

    red = "".join(red)
    red = red[::-1]
    blue = "".join(blue)

    red = list(red)
    red.reverse()
    return (red, explosiveRed, mistake, list(blue), explosiveBlue)

    print("Red Team :")
    print(len(red))
    if len(red) == 0:
        print("Empty")
    else:
        print(red)
    print(f'{explosiveRed} Explosive(s) ! ! ! (HEAT)')
    if mistake > 0:
        print(f'Blue Team Made (a) Mistake(s) {mistake} Bomb(s)')
    print("----------TENETTENET----------")
    print(": maeT eulB")
    print(freeze)
    if len(blue) == 0:
        print("ytpmE")
    else:
        print(blue)
    print(f'(EZEERF) ! ! ! (s)evisolpxE {explosiveBlue}')