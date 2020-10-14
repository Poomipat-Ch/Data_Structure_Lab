class LinkedList:
    class Node:
        def __init__(self, data, next = None):	#สร้างโหนดเพื่อเก็บข้อมูล
            self.data = data
            if next is None:
                self.next = None
            else:
                self.next = next
    def __init__(self):					#สร้าง linked list ว่าง
        self.header = self.Node(None, None)
        self.size = 0
 
    def __str__(self):					#แสดงข้อมูลจากหัวไปหาง
        s = 'LinkedList data : '
        p = self.header.next
        while p != None:
            s += str(p.data) + ' '
            p = p.next
        return s
 
    def __len__(self):	return self.size		#ส่งค่าจำนวนสมาชิก
        
    def isEmpty(self):	return self.size == 0	#ตรวจสอบลิสต์ว่าง
        
    def indexOf(self,data):				#หา index ของข้อมูล data
        q = self.header.next
        for i in range(len(self)):
            if q.data == data:
                return i
            q = q.next
        return -1
    
    def isIn(self,data):				#ส่งค่า True ถ้า linked list ว่าง, False ถ้าไม่ว่าง
        return self.indexOf(data) >= 0
    
    def nodeAt(self, i):				#หาตำแหน่งโหนดที่ index i
        p = self.header
        for j in range(-1,i):
            p = p.next
        return p
    
    def append(self, data):				#เพิ่มข้อมูลต่อท้าย
        return self.insertAfter(len(self),data)
 
    def insertAfter(self, i, data):			#เพิ่มข้อมูลหลังโหนด index i
        p = self.nodeAt(i-1)
        p.next = self.Node(data, p.next)
        self.size += 1
    
    def add(self, data):				#เพิ่มข้อมูลแบบเรียงลำดับจากน้อยไปมาก
        if not self.isEmpty():
            i = 0
            p = self.header.next
            for i in range(len(self)):
                if data > p.data:
                    p = p.next
                    i += 1
                else:
                    self.insertAfter(i, data)
                    return
        self.insertAfter(len(self), data)
    
    def deleteAfter(self, i):				#ลบโหนดหลัง index i
        p = self.nodeAt(i)
        tmp = p.next
        p.next = p.next.next
        self.size -= 1
        return tmp
    
    def removeDup(self):				#นำข้อมูลตัวซ้ำออก
        dup = dict()
        p = self.header.next
        size = len(self)
        for i in range(size):
            tmp = self.deleteAfter(-1)
            dup[tmp.data] = dup.get(tmp.data, 0) + 1
        for j in dup.keys():
            self.append(j)
        
        
 
def findMean(l):
    sum = 0
    p = l.header.next
    for i in range(len(l)):
        sum += p.data
        p = p.next
    print("Mean = %.2f" % (sum/len(l)))
 
def findMode(l):
    dup = dict()
    p = l.header.next
    mode = []
    for i in range(len(l)):
        dup[p.data] = dup.get(p.data, 0) + 1
        p = p.next
    maxVal = 2
    for key, val in dup.items():
        if val > maxVal:
            maxVal = val
            while len(mode) > 0:
                mode.pop()
            mode.append(str(key))
        elif val == maxVal:
            mode.append(str(key))
    print(("Mode = "+", ".join(mode)) if len(mode) > 0 else "Mode is not available.")
 
def findMedian(l):
    if len(l) % 2 == 0:
        p1 = l.nodeAt(len(l)//2).data
        p2 = l.nodeAt(len(l)//2-1).data
        print("Median = %.2f" % ((p1+p2)/2))
    else:
        p = l.nodeAt(len(l)//2).data
        print("Median %.2f" % p)
    
num = input("Enter 12 number : ").split()
l = LinkedList()
for e in num:
    l.add(int(e))
print('Output :\n'+str(l))
findMean(l)
findMode(l)
findMedian(l)
