class Queue:
    
    def __init__(self, lists = None):
        self.lists = [] if lists == None else lists
    
    def enqueue(self, item):
        print(f'Add {item} index is {self.size()}')
        self.lists.append(item)
    
    def dequeue(self):
        return self.lists.pop(0) if not self.isEmpty() else -1

    def isEmpty(self):
        return self.lists == []
    
    def size(self):
        return len(self.lists)

    def __str__(self):
        if self.size() > 0:
            return str(self.lists)
        else:
            return 'Empty'


if __name__ == "__main__":
    n = input('Enter Input : ').split(',')
    q = Queue()
    
    for i in n:
        i = i.split()
        if i[0] == 'E':
            q.enqueue(i[1])
        else:
            print(f'Pop {q.dequeue()} size in queue is {q.size()}' if not q.isEmpty() else -1)
    print(f'Number in Queue is :  {q}' if not q.isEmpty() else q)
