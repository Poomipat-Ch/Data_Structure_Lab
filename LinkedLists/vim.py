class Node:
    def __init__(self,data, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous
    
class LinkedList:
    def __init__(self):
        self.tail = self.head = Node('|')
        cur = Node('|')
        self.size_ = 1
        self.indexCur = 0

    def __str__(self):
        p = self.head
        toText = []
        while p is not None:
            toText.append(p.data)
            p = p.next
        return " ".join(toText)
    
    def addBefore(self, data):
        p = self.head
        newNode = Node(data)
        while p is not None:
            if p.data == '|':
                break
            p = p.next
        newNode.next = p
        newNode.previous =p.previous
        if p.previous is not None:
            p.previous.next = newNode
        p.previous = newNode
        if self.size_ == 1:
            self.head = newNode
        self.size_ += 1
        self.indexCur += 1
        
        

    def curLeft(self):
        p = self.head
        if self.indexCur != 0:
            while p is not None:
                if p.data == '|':
                    break
                p = p.next
            if p.previous.previous is not None:
                p.previous.previous.next = p
            else:
                self.head = p
            p.previous.next = p.next
            if p.next is not None:
                p.next.previous = p.previous
            p.next = p.previous
            p.previous = p.previous.previous
            self.indexCur -= 1
    
    def curRight(self):
        p = self.head 
        if self.indexCur != self.size_ - 1:
            while p is not None:
                if p.data == '|':
                    break
                p = p.next
            if p.next.next is not None:
                p.next.next.previous = p
            else:
                self.tail = p
            p.next.previous = p.previous
            if p.previous is not None:
                p.previous.next = p.next
            else:
                self.head = p.next
            p.previous = p.next
            p.next = p.next.next
            p.previous.next = p
            self.indexCur += 1
    
    def deleteLeft(self):
        p = self.head
        if self.indexCur != 0:
            while p is not None:
                if p.data == '|':
                    break
                p = p.next
            if p.previous.previous is not None:
                p.previous.previous.next = p
            else:
                self.head = p
            if p.next is not None:
                p.next.previous = p.previous.previous
            p.previous = p.previous.previous
            self.size_ -= 1
            self.indexCur -= 1

    def deleteRight(self):
        p = self.head
        if self.indexCur != self.size_ - 1:
            while p is not None:
                if p.data == '|':
                    break
                p = p.next
            if p.next.next is not None:
                p.next.next.previous = p
            else:
                self.tail = p
            if p.previous is not None:
                p.previous.next = p
            else:
                self.head = p
            p.next = p.next.next
            self.size_ -= 1
        

if __name__ == "__main__":
    n = input('Enter Input : ').split(',')

    ll = LinkedList()
    for data in n:
        data = data.split()
        if data[0] == 'I':
            ll.addBefore(data[1])
        elif data[0] == 'L':
            ll.curLeft()
        elif data[0] == 'R':
            ll.curRight()
        elif data[0] == 'B':
            ll.deleteLeft()
        else:
            ll.deleteRight()
    
    print(ll)
