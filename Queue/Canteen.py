class Queue:
    
    def __init__(self, lists = None):
        self.lists = [] if lists == None else lists
    
    def enqueue(self, item):
        for i in self.lists[-1::-1]:
            if i[0] == item[0]:
                if self.lists.index(i) == self.size() - 1:
                    break
                self.lists.insert(self.lists.index(i) + 1, item)
                return
        self.lists.append(item)
    
    def dequeue(self):
        return self.lists.pop(0)[1] if not self.isEmpty() else 'Empty'

    def isEmpty(self):
        return self.lists == []
    
    def size(self):
        return len(self.lists)

    def __str__(self):
        if self.size() > 0:
            return str(self.lists)
        else:
            return 'Empty'

# if __name__ == "__main__":
def canteenPooM(n):
    # n = input('Enter Input : ').split('/')
    result = ''
    emp = dict()
    totalsize = 0
    for i in n[0].split(','):
        i = i.split()
        emp[int(i[1])] = emp.get(int(i[1]),int(i[0]))

    q = Queue()
    for i in n[1].split(','):
        i = i.split()
        if i[0] == 'E':
            i[0] = emp[int(i[1])]
            q.enqueue(i)
        else:
            result += ' '+q.dequeue()

    return result
                