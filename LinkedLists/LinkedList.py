
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next if next != None else None

class LinkedList:
            
    def __init__(self, head = None):
        if head is None:
            self.head = self.tail = None
            self.size_ = 0
        else:
            self.head = head
            t = self.head
            self.size_ = 1
            while t.next != None:
                t = t.next
                self.size_ += 1
            self.tail = t

    def append(self, item):
        p = Node(item)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
        self.tail = p
        self.size_ += 1
    
    def addHead(self, item):
        p = Node(item)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            self.head = p
            p.next = t
        self.size_ += 1

    def remove(self, item):
        t = self.head
        if t.data == item:
            return self.removeHead()
        else:
            while t.next != None:
                if t.next.data == item:
                    removed = t.next
                    t.next = t.next.next
                    self.size_ -= 1
                    return removed
    
    def removeTail(self):
        t = self.before(self.tail.data)
        removed = t.next
        t.next = None
        self.size_ -= 1
        return removed
    
    def removeHead(self):
        t = self.head
        self.head = t.next
        self.size_ -= 1
        return t

    def deleteAfter(self, i):
        t = self.nodeAt(i)
        t.next = t.next.next
        self.size_ -= 1
    
    def nodeAt(self, i):
        t = self.head
        for j in range(i):
            t = t.next
        return t

    def search(self, item):
        t = self.head
        while t.next != None:
            if t.data == item:
                return t
            t = t.next
        return None
        
    def size(self):
        return self.size_

    def isEmpty(self):
        return True if self.size() == 0 else False

    def isIn(self, item):
        t = self.head
        if t.data == item:
            return True
        while t.next != None:
            if t.data == item:
                return True
            t = t.next
        return False

    def before(self, item):
        t = self.head
        while t.next != None:
            if t.next.data == item:
                return t
            t = t.next
        return None

    def insertAfter(self, index, item):
        t = self.nodeAt(index)
        p = Node(item)
        p.next = t.next
        t.next = p
        self.size_ += 1
    
    def __str__(self):
        lst = []
        t = self.head
        while t.next != None:
            lst.append(t.data)
            t = t.next
        lst.append(t.data)
        return ','.join(lst)
