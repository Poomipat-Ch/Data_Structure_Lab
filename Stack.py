class Stack:

    def __init__(self, li = []):
        self.li = li
    
    def push(self,element):
        self.li.append(element)
    def pop(self):
        return self.li.pop()



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