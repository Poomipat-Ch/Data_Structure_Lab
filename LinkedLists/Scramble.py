class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

def createLL(LL):
    head = Node(LL.pop(0))
    p = head
    while len(LL) > 0:
        p.next = Node(LL.pop(0))
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
    p = head
    buttom = []
    for _ in range(int(size*b//100)):
        buttom.append(p.value)
        p = p.next
    head = p
    
    p = head
    while len(buttom) > 0:
        if p.next is None:
            p.next = Node(buttom.pop(0))
        p = p.next

    t = p = head
    buttom = []
    while p is not None:
        buttom.append(p.value)
        p = p.next
    print(f"BottomUp {b:.3f} % : "+ " ".join(buttom))

    riffle = []
    p = t
    for _ in range(int(size*r//100)):
        riffle.append(p.value)
        p = p.next

    size_after_riffer = SIZE(p)
    x = Node(riffle.pop(0))
    x.next = p
    h = p = x
    size_ = SIZE(p)
    for i in range(size_ + 1):
        if i % 2 == 1:
            x = Node(riffle.pop(0))
            x.next = p.next
            p.next = x
        p = p.next
    p = p.next

    size_riffle = 0
    while len(riffle) > 0:
        size_riffle += 1
        x = Node(riffle.pop(0))
        p.next = x
        p = p.next

    print(f"Riffle {r:.3f} % :",printLL(h))
    
    deRiffle = []
    p = h
    t = p.next
    for i in range(int(size*r//100)+1):
        if i % 2 == 0:
            deRiffle.append(p.value)
        p = p.next
    p = p.next
    for _ in range(size_riffle):
        deRiffle.append(p.value)
        p = p.next
    p = t
    for _ in range(size_after_riffer-1):
        t.next = t.next.next
        t = t.next
    t.next = None
    
    t = x = Node(deRiffle.pop(0))
    while len(deRiffle) > 0:
        x.next = Node(deRiffle.pop(0))
        x = x.next
    x.next = p
    print(f"Deriffle {r:.3f} % :",printLL(t))
    
    deButtom = []
    x = x.next.next
    while x is not None:
        deButtom.append(x.value)
        x = x.next
    p.next = None
    p = y = Node(deButtom.pop(0))
    while len(deButtom) > 0:
        y.next = Node(deButtom.pop(0))
        y = y.next
    y.next = t
    print(f"Debottomup {b:.3f} % :",printLL(p))


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