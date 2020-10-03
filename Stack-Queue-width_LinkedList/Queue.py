from LinkedList import LinkedList
class Queue:
    def __init__(self):
        self.items = LinkedList()
    
    def __str__(self):
        return str(self.items)
    
    def enqueue(self, data):
        self.items.push_back(data)

    def dequeue(self):
        return self.items.pop_front()
    
    def isEmpty(self):
        return self.items.isEmpty()
    
    def size(self):
        return self.items.size()