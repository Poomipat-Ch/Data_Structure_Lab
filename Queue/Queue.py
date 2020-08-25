class Queue:
    
    def __init__(self, lists = None):
        self.lists = [] if lists == None else lists
    
    def enqueue(self, item):
        self.lists.append(item)
    
    def dequeue(self):
        return self.lists.pop(0) if not self.isEmpty() else "มันหมดแล้ว"

    def isEmpty(self):
        return self.lists == []
    
    def size(self):
        return len(self.lists)