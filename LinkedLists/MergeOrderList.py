class node:
    def __init__(self,data,next = None ):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

def createList(l=[]):
    n = node(int(l.pop(0)))
    head = n 
    while len(l) > 0:
        n.next = node(int(l.pop(0)))
        n = n.next
    return head

def printList(H):
    data = []
    while H is not None:
        data.append(str(H.data))
        H = H.next
    print(' '.join(data))

head = None
def mergeOrderesList(p,q):
    while p is not None:
        sorts(p.data)
        p = p.next
    while q is not None:
        sorts(q.data)
        q = q.next
    return head

def sorts(data):
        global head
        curr = head
        if curr is None:
            n = node(data)
            head = n
            return

        if curr.data > data:
            n = node(data)
            n.next = curr
            head = n
            return

        while curr.next is not None:
            if curr.next.data > data:
                break
            curr = curr.next
        n = node(data)
        n.next = curr.next
        curr.next = n
        return

#################### FIX comand ####################   
L1,L2 = map(str,input("Enter 2 Lists : ").split())
LL1 = createList(L1.split(','))
LL2 = createList(L2.split(','))
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)