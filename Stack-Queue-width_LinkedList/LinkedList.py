class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail
        self.size_ = 0

    def __str__(self):
        buff = self.head.next
        lst = []
        while buff is not self.tail:
            lst.append(buff.data)
            buff = buff.next
        return "Size : "+str(self.size_)+" Lists : "+"->".join([str(i) for i in lst])

    def size(self):
        return self.size_

    def isEmpty(self):
        return self.size() == 0

    def push_back(self, data):
        p = self.tail.prev
        newNode = Node(data,self.tail,p)
        p.next = newNode
        self.tail.prev = newNode
        self.size_ += 1

    def push_front(self, data):
        p = self.head.next
        newNode = Node(data,p,self.head)
        p.prev = newNode
        self.head.next = newNode
        self.size_ += 1
    
    def pop_back(self):
        if self.size() > 0:
            tmp = self.tail.prev
            self.tail.prev = tmp.prev
            tmp.prev.next = self.tail
            tmp.next = tmp.prev = None
            self.size_ -= 1
            return tmp.data
        else:
            return "Error : Empty List"
    
    def pop_front(self):
        if self.size() > 0:
            tmp = self.head.next
            self.head.next = tmp.next
            tmp.next.prev = self.head
            tmp.next = tmp.prev = None
            self.size_ -= 1
            return tmp.data
        else:
            return "Error : Empty List"

    def pop(self, data):
        if self.size() > 0:
            p = self.head.next
            while p is not self.tail:
                if p.data == data:
                    buff = p.prev
                    buff.next = p.next
                    p.next.prev = buff
                    p.next = p.prev = None
                    self.size_ -= 1
                    return p.data
                p = p.next
            return "Not Found!!!"
        else:
            return "Error : Empty List"

    def insert(self, index, data):
        p = self.NodeAt(index)
        if type(p) == Node:
            newNode = Node(data, p, p.prev)
            p.prev.next = newNode
            p.prev = newNode
            self.size_ += 1
        else:
            print("Error : "+p)
    
    def NodeAt(self, index):
        p = self.head.next
        if index < 0:
            index = self.size() + index
        elif index > self.size():
            return "Out of Range!!!"

        for _ in range(index):
            p = p.next
        return p
