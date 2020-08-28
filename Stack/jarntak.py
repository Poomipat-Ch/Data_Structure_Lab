class Stack:

    def __init__(self, li = None):
        self.item_list = [] if li == None else li
    
    def push(self,ele):
        self.item_list.append(ele)
    
    def pop(self):
        return self.item_list.pop()

    def peek(self):
        return self.item_list[self.size() - 1]
    
    def isEmpty(self):
        return True if self.item_list == [] else False

    def size(self):
        return len(self.item_list)

if __name__ == "__main__":
    n = input('Enter Input : ').split(',')
    j = dict()
    s = Stack()
    weight = []
    for i in n:
        j[i.split()[1]] = j.get(i.split()[1],0)+int(i.split()[0])
        weight.append(i.split()[1])
    for i in weight:
       # print(s.item_list)
        if s.isEmpty():
            s.push(i)
        elif j[s.peek()] >= j[i]:
            s.push(i)
        else:
            while  not s.isEmpty() and j[s.peek()] < j[i] :
                print(s.pop())
            s.push(i)