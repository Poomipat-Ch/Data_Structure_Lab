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
    tree = []
    s = Stack()
    for i in n:
        if i == 'B':
            print(''.join(s.item_list))
        elif 
            
