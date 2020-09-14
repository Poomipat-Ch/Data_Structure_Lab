class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self, root = None):
        self.head = None if root is None else root
        self.tail = None
        self.size_ = 0
        if self.head is not None:
            p = self.head
            while p.next != None:
                self.size_ += 1
                p = p.next
            self.tail = p
    
    def __str__(self):
        totext = ""
        if self.head is not None and self.size_ > 0:
            p = self.head
            data = []
            while p.next != None:
                data.append(p.data)
                p = p.next
            data.append(p.data)
            totext = "link list : " + "->".join(data)
        else:
            totext = "List is empty"
        return totext

    def isEmpty(self):
        return True if self.head is None and self.tail is None and self.size_ == 0 else False

    def append(self, data):
        newNode = Node(data)
        if self.size_ == 0:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size_ += 1

    def insert(self, index, data):
        p = self.head
        newNode = Node(data)
        if index < 0 or index > self.size_ + 1 or (self.isEmpty() and index != 0):
            print("Data cannot be added")
            return
        print(f"index = {index} and data = {data}")
        if index == 0:
            newNode.next = p
            self.head = newNode
            self.size_ += 1
            return
        else:
            for _ in range(index-1):
                    p = p.next
            newNode.next = p.next
            p.next = newNode
            self.size_ += 1


if __name__ == "__main__":
    n = input("Enter Input : ").split(',')

    ll = LinkedList()
    for i in n[0].split():
        if i is None:
            print("List is empty")
            break
        ll.append(i)
    print(ll)
    
    for i in  n[1:]:
        i = i.split(':')
        ll.insert(int(i[0]),i[1])
        print(ll)