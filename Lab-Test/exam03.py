class DoublyLinkedList:
    class Node:
        def __init__(self,data,prev = None,next = None):
            self.data = data
            if prev is None:
                self.prev = None
            else:
                self.prev = prev
            if next is None:
                self.next = None
            else:
                self.next = next
    
    def __init__(self):
        self.header = self.Node(None,None,None)
        self.header.next = self.header
        self.size = 0
    
    def __str__(self):			#ใช้ เหมือนกับ class LinkedList
        p = self.header.next
        text = []
        while p is not None:
            text.append(p.data)
            p = p.next
        return " ".join(text)

    def __len__(self):			#ใช้ เหมือนกับ class LinkedList
        return self.size

    def isEmpty(self):			#ใช้ เหมือนกับ class LinkedList
        return self.header.next == None and self.size == 0

    def indexOf(self,data):			#ใช้ เหมือนกับ class LinkedList
        p = self.header.next
        i = 0
        while p is not None:
            if p.data == data:
                return i
            p = p.next
            i += 1
        return -1

    def isIn(self,data):			#ใช้ เหมือนกับ class LinkedList
        return self.indexOf(data) >= 0

    def nodeAt(self,i):			#ใช้ เหมือนกับ class LinkedList
        p = self.header.next
        for _ in range(i):
            p = p.next
        return p
 
    def insertBefore(self, q, data):
        p = q.prev
        x = self.Node(data,p,q)
        p.next = q.prev = x
        self.size += 1
    
    def append(self,data):
        self.insertBefore(self.nodeAt(self.size),data)
 
    def add(self,i,data):
        self.insertBefore(self.nodeAt(i),data)
 
    def remove(self,data):
        q = self.header.next
        while q != self.header:
            if q.data == data:
                self.removeNode(q)
                return 0
            q = q.next
        return -1
    
    def removeNode(self,p):
        prev = p.prev
        prev.next = p.next.next
        if p.next.next is not None:
            p.next.next.prev = prev
        p.next = p.prev = None
        self.size -= 1
 
class Queue:
    def __init__(self,q = None):
        if q == None:
            self.item = DoublyLinkedList()
        else:
            self.item = q
 
    def __str__(self):
        s = 'Queue data : '
        st = str((self.item))
        s += str(st[18:])
        return s
 
    def __len__(self) : 
        return len(self.item)
    
    def isEmpty(self) : 
        return self.item.isEmpty()
 
    def enQueue(self,data):
        self.item.append(data)
    
    def enQueueLeft(self,data):
        self.item.insertBefore(self.item.nodeAt(0), data)

    def deQueue(self):
        self.item.removeNode(self.item.nodeAt(0))
 
    def deQueueRight(self):
        self.item.removeNode(self.item.nodeAt(len(self.item) - 1))

ll = DoublyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
print(ll)