class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    
    def __init__(self, size, MaxCollision):
        self.size = size
        self.count_insert = 0
        self.MaxCollision = MaxCollision
        self.conllision = 0
        self.lst = [None for _ in range(self.size)]
    
    def append(self, key, value):
        sum_ascii = 0
        newData = Data(key, value)
        for i in key:
            sum_ascii += ord(i)
        index = sum_ascii % self.size
        if self.lst[index] is None:
            self.lst[index] = newData
            self.printTable()
            self.count_insert += 1
            self.conllision = 0
        elif self.count_insert == len(self.lst):
            print("This table is full !!!!!!")
            quit()
        else:
            self.conllision += 1
            print(f'collision number {self.conllision} at {index}')
            self._append(index, (index+self.conllision**2)%self.size, newData)
    
    def _append(self, index, duplicate, newData):
        if self.lst[duplicate] is None:
            self.lst[duplicate] = newData
            self.conllision = 0
            self.count_insert += 1
            self.printTable()
        elif self.conllision <= self.MaxCollision:
            self.conllision += 1
            print(f'collision number {self.conllision} at {duplicate}')
            if self.conllision == self.MaxCollision:
                print("Max of collisionChain")
                self.conllision = 0
                self.printTable()
                return
            self._append(index, (index + self.conllision**2)%self.size, newData)

    def printTable(self):
        for i in range(1,len(self.lst)+1):
            print(f"#{i}	{self.lst[i-1]}")
        print('---------------------------')
            



left, right = input(" ***** Fun with hashing *****\nEnter Input : ").split('/')
size, maxCollision = map(int,left.split())
data = right.split(',')
H = hash(size,maxCollision)
for i in range(len(data)):
    x = data[i].split()
    H.append(x[0],x[1])
