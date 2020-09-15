class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

def createLL(LL):
    head = Node(LL[0])
    p = head
    for i in range(1,len(LL)):
        p.next = Node(LL[i])
        p.next.prev = p
        p = p.next
    return head
    
        

def printLL(head):
    p = head
    toText = []
    while p is not None:
        toText.append(p.value)
        p = p.next
    return " ".join(toText)

def SIZE(head):
    p = head
    size = 0
    while p is not None:
        size += 1
        p = p.next
    return size



def scarmble(head, b, r, size):
    tail = head_p = p = head
    while tail.next is not None:
        tail = tail.next
    lst_buttom = []
    for _ in range(int(size*b//100)):
        lst_buttom.append(p.value)
        p = p.next
    
    connect_buttom = createLL(lst_buttom)
    tail.next = connect_buttom
    print(f"BottomUp {b:.3f} % :",printLL(p))

    lst_riffle = []
    head_p1 = p
    for _ in range(int(size*r//100)):
        lst_riffle.append(p.value)
        p = p.next

    lst_riffle1 = []
    while p is not None:
        lst_riffle1.append(p.value)
        p = p.next
    
    i = 0
    lst_riffle_last = []
    while len(lst_riffle) > 0 and len(lst_riffle1) > 0:
        if i % 2 == 1:
            lst_riffle_last.append(lst_riffle1.pop(0))
        else:
            lst_riffle_last.append(lst_riffle.pop(0))
        i += 1
    
    if len(lst_riffle) > 0:
        lst_riffle_last += lst_riffle
    elif len(lst_riffle1) > 0:
        lst_riffle_last += lst_riffle1
    riffle = createLL(lst_riffle_last)
    print(f"Riffle {r:.3f} % :",printLL(riffle))

    from_riffle = riffle
    lst_deRiffle = [[],[]]
    for _ in range(int(size*r//100)):
        if from_riffle.next is not None:
            lst_deRiffle[1].append(from_riffle.value)
            from_riffle = from_riffle.next
        if from_riffle.next is not None and len(lst_deRiffle[0]) < size - int(size*r//100):
            lst_deRiffle[0].append(from_riffle.value)
            from_riffle = from_riffle.next
    while len(lst_deRiffle[1]) < int(size*r//100):
        lst_deRiffle[1].append(from_riffle.value)
        if from_riffle.next is not None:
            from_riffle = from_riffle.next
        else:
            break
    while len(lst_deRiffle[0]) < size - int(size*r//100):
        lst_deRiffle[0].append(from_riffle.value)
        if from_riffle.next is not None:
            from_riffle = from_riffle.next
        else:
            break
    
    riffle1,riffle2 = createLL(lst_deRiffle[1]), createLL(lst_deRiffle[0])
    riffle1_tail = riffle1
    while riffle1_tail.next is not None:
        riffle1_tail = riffle1_tail.next
    riffle1_tail.next = riffle2
    deRiffle = riffle1
    print(f"Deriffle {r:.3f} % :",printLL(deRiffle))


    lst_deButtom = []
    head_deButtom = bottom = tail.next
    while bottom.next is not None:
        lst_deButtom.append(bottom.value)
        bottom = bottom.next
    lst_deButtom.append(bottom.value)
    tail.next = None
    de_buttom = createLL(lst_deButtom)
    bottom.next = head_p1

    print(f"Debottomup {b:.3f} % :",printLL(head_deButtom))
    
if __name__ == "__main__":
    inp1, inp2 = input('Enter Input : ').split('/')
    print('-' * 50)
    h = createLL(inp1.split())
    for i in inp2.split('|'):
        print("Start : {0}".format(printLL(h)))
        k = i.split(',')
        if k[0][0] == "B" and k[1][0] == "R":
            scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
        elif k[0][0] == "R" and k[1][0] == "B":
            scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
        print('-' * 50)
