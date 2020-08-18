class Stack:

    def __init__(self, li = None):
        self.item_list = [] if li == None else li
    
    def push(self,ele):
        self.item_list.append(ele)
    
    def pop(self):
        return self.item_list.pop()

    def peek(self):
        return self.item_list[len(self.item_list-1)]
    
    def isEmpty(self):
        return True if self.item_list == [] else False
    def size(self):
        return len(self.item_list)


if __name__ == '__main__':
    a = Stack()
    a.push(5)
    a.push(20)
    a.push('555')
    print(a.pop())
    print(a.li)
    print(a.pop())
    print(a.li)
    print(a.pop())
    print(a.li)