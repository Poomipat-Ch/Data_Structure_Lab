class Queue:
    
    def __init__(self, lists = None):
        self.lists = [] if lists == None else lists
    
    def enqueue(self, *item):
        for i in item:
            self.lists.append(i)
    def dequeue(self):
        return self.lists.pop(0) if not self.isEmpty() else -1

    def dequeueLast(self):
        return self.lists.pop() if not self.isEmpty() else -1

    def isEmpty(self):
        return self.lists == []
    
    def size(self):
        return len(self.lists)

    def __str__(self):
        if self.size() > 0:
            return str(self.lists)
        else:
            return 'Empty'



if __name__ == "__main__":
    n = input('Enter Input (Red, Blue) : ').split()
    red = list(n[0])
    blue = list(n[1])
    blue_freeze = Queue()
    red_explotion = Queue()
    blue_mistake = 0
    blue_bomb = 0
    red_explosive = 0

    finished = False
    temp = []
    while not finished:
        if len(blue) > 2:
            if blue[0] == blue[1] == blue[2]:
                blue_bomb += 1
                blue_freeze.enqueue(blue.pop(0))
                blue.pop(0)
                blue.pop(0)
            else:
                temp.append(blue.pop(0))
        elif len(blue) > 0:
            temp.append(blue.pop(0))
        else:
            finished = True

    while len(temp) > 0:
        blue.append(temp.pop(0))
    

    finished = False
    while not finished:
        if len(red) > 0:
            if len(red) > 2:
                if red[0] == red[1] == red[2]:
                    if not blue_freeze.isEmpty():
                        blue_last = blue_freeze.dequeueLast()
                        if red[0] == blue_last:
                            blue_mistake += 1
                            red.pop(0)
                            red.pop(0)
                            red_explotion.enqueue(red.pop(0))
                        else:
                            red_explotion.enqueue(red.pop(0),red.pop(0),blue_last,red.pop(0))
                    else:
                        red_explosive += 1
                        red.pop(0)
                        red.pop(0)
                        red.pop(0)
                else:
                    red_explotion.enqueue(red.pop(0))
            else:
                red_explotion.enqueue(red.pop(0))
        else:
            finished = True
    print('Red Team :')
    print(red_explotion.size())
    if red_explotion.isEmpty():
        print('Empty', end="")
    while not red_explotion.isEmpty():
            print(red_explotion.dequeueLast(), end="")
    
    print(f'\n{red_explosive} Explosive(s) ! ! ! (HEAT)')
    if blue_mistake > 0:
        print(f'Blue Team Made (a) Mistake(s) {blue_mistake} Bomb(s)')
    print('----------TENETTENET----------')
    print(f': maeT eulB\n{len(blue)}')
    print("".join(blue if len(blue) > 0 else 'ytpmE'))
    print(f'(EZEERF) ! ! ! (s)evisolpxE {blue_bomb}')