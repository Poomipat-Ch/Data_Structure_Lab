class hash:
    
    def __init__(self, size, MaxCollision, threshold):
        self.size = size
        self.threshold = threshold
        self.count_insert = 0
        self.MaxCollision = MaxCollision
        self.collision = 0
        self.tmp_data = []
        self.lst = [None for _ in range(self.size)]
        print("Initial Table :")
        self.printTable()
    
    def append(self, key):
        if key not in self.tmp_data:
            print("Add :",key)
            self.tmp_data.append(key)
        
        index = key % self.size
        
        for i in range(self.MaxCollision):
            new_index = (index+ (i**2)) % self.size
            if self.lst[new_index] is None:
                self.lst[new_index] = key
                self.count_insert += 1
                self.collision = 0
                break
            else:
                self.collision += 1
                print(f"collision number {i+1} at {new_index}")

        if (self.count_insert/self.size)*100 > self.threshold:
            print('****** Data over threshold - Rehash !!! ******')
            self.rehash()
        elif self.collision == self.MaxCollision:
            print('****** Max collision - Rehash !!! ******')
            self.rehash()

    def rehash(self):
        self.size = self.nearest_prime()
        self.lst = [None] * self.size
        self.count_insert = 0
        for i in self.tmp_data:
            self.append(i)

    def printTable(self):
        for i in range(1,len(self.lst)+1):
            print(f"#{i}	{self.lst[i-1]}")
        print('----------------------------------------')


    def nearest_prime(self):
        nearest = self.size*2
        while True:
            i = 2
            prime = True
            while i <= nearest**0.5:
                if nearest % i == 0:
                    prime = False
                    break
                i += 1
            if prime:
                break
            nearest += 1
        return nearest


prop, arr = input(" ***** Rehashing *****\nEnter Input : ").split('/')
size, max_conllision, threshold = list(map(int,prop.split()))
datas = list(map(int,arr.split()))
rh = hash(size,max_conllision,threshold)
for i in datas:
    rh.append(i)
    rh.printTable()