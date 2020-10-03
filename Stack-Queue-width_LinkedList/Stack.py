from LinkedList import LinkedList

class Stack:
    def __init__(self):
        self.items = LinkedList()
    
    def __str__(self):
        return str(self.items)
    
    def push(self, data):
        self.items.push_back(data)
    
    def pop(self):
        return self.items.pop_back()

    def peek(self):
        return self.items.NodeAt(-1).data
    
    def size(self):
        return self.items.size()
    
    def isEmpty(self):
        return self.items.isEmpty()