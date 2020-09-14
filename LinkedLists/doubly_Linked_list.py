class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None
    
class LinkedList:
    def __init__(self):
        self.head = self.tail = Node(None)
        self.size_ = 0
    
    def __str__(self):
        toSend = "linked list : "
        if self.size_ > 0:
            p = self.head
            data = []
            while p.next is not None:
                data.append(p.data)
                p = p.next
            data.append(p.data)
            return toSend + "->".join(data)
        return toSend    
    
    def str_reverse(self):
        toSend = "reverse : "
        if self.size_ > 0:
            p = self.tail
            data = []
            while p.previous.previous is not None:
                data.append(p.data)
                p = p.previous
            data.append(p.data)
            return toSend + "->".join(data)
        return toSend 

    def is_empty(self):
        return True if self.size_ == 0 else False
    
    def append(self, data):
        newNode = Node(data)
        self.tail.next = newNode
        newNode.previous = self.tail
        self.tail = newNode
        self.size_ += 1
        if self.size_ == 1:
            self.head = newNode

    def add_before(self, data):
        newNode = Node(data)
        if self.is_empty():
            newNode.previous = self.head
            self.head.next = newNode
            self.tail = newNode
        else:
            newNode.previous = self.head.previous
            self.head.previous = newNode
            newNode.next = self.head
        self.head = newNode
        self.size_ += 1
        
    
    def insert(self, index, data):
        newNode = Node(data)
        p = self.head

        if index > self.size_ or index < 0:
            print("Data cannot be added")
            return

        if self.is_empty() and index == 0:
            p.next = newNode
            newNode.previous = p
            self.head = self.tail = newNode
            self.size_ += 1
            print(f"index = {index} and data = {data}")
            return

        if index == self.size_:
            newNode.previous = self.tail
            self.tail.next = newNode
            self.tail = newNode
            self.size_ += 1
            print(f"index = {index} and data = {data}")
            return


        i = 0
        while i < index:
            p = p.next
            i += 1
        newNode.previous = p.previous
        p.previous.next = newNode
        newNode.next = p
        p.previous = newNode
        if index == 0:
            self.head = newNode
        self.size_ += 1
        print(f"index = {index} and data = {data}")

            

    def remove(self, data):
        p = self.head
        i = 0
        while p is not None:
            if p.data == data:
                p.previous.next = p.next
                if p is not self.tail: 
                    p.next.previous = p.previous
                else:
                    self.tail = p.previous
                if i == 0:
                    self.head = p.next if p.next is not None else p.previous
                self.size_ -= 1
                print(f"removed : {data} from index : {i}")
                return
            p = p.next
            i += 1
        print("Not Found!")


if __name__ == "__main__":
    n = input("Enter Input : ").split(',')
    ll = LinkedList()
    for i in n:
        i = i.split()
        if i[0] == 'Ab':
            ll.add_before(i[1])
        elif i[0] == 'I':
            i[1] = i[1].split(':')
            ll.insert(int(i[1][0]),i[1][1])
        elif i[0] == 'R':
            ll.remove(i[1])
        else:
            ll.append(i[1])
        print(ll)
        print(ll.str_reverse())
    
