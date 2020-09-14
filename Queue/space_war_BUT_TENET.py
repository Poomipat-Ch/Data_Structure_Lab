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

def check_bomb(bomb, freeze = None):
    temp = [bomb.dequeue() for _ in range(bomb.size())]
    explosive = 0
    while True:
        if bomb.size() > 2:
            a, b, c = bomb.dequeueLast(),bomb.dequeueLast(),bomb.dequeueLast()
            if a == b == c:
                explosive += 1
                if freeze != None:
                    freeze.enqueue(a)
            else:
                bomb.enqueue(c,b,a)
                if len(temp) > 0:
                    bomb.enqueue(temp.pop(0))
        else:
            if len(temp) > 0:
                bomb.enqueue(temp.pop(0))

        if len(temp) == 0:
            lst = [bomb.dequeueLast(),bomb.dequeueLast(),bomb.dequeueLast()]
            if lst[0] == lst[1] == lst[2] != -1:
                explosive += 1
                if freeze != None:
                    freeze.enqueue(a)
            else:
                for a in reversed(lst):
                    if a!= -1:
                        bomb.enqueue(a)
                        
                if len(temp) > 0:
                    bomb.enqueue(temp.pop(0))
            break

    return explosive
    
# if __name__ == '__main__':
#     n = input('Enter Input (Red, Blue) : ').split()
#     red = list(n[0])
#     blue = list(n[1])
def space_war_BUT_TENET(r, b):
    red, blue = list(r), list(b)
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
            x = blue.pop(0)
            if x != -1:
                temp.append(x)
        else:
            finished = True

    while len(temp) > 0:
        blue.append(temp.pop(0))
    blue_bomb += check_bomb(Queue(blue),blue_freeze)
    print(blue_freeze.lists)

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
                        else:
                            red_explotion.enqueue(red.pop(0),red.pop(0),blue_last)
                        red_explotion.enqueue(red.pop(0))
                    else:
                        red_explosive += 1
                        red.pop(0)
                        red.pop(0)
                        red.pop(0)
                else:
                    a = red.pop(0)
                    red_explotion.enqueue(a)
            else:
                x = red.pop(0)
                if x != -1:
                    red_explotion.enqueue(x)
        else:
            finished = True

    red_explosive += check_bomb(red_explotion)

    return (red_explotion.lists, red_explosive, blue_mistake, blue, blue_bomb)

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