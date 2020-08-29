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
    tree = Stack()
    canSee = Stack()

    for i in n:
        i = i.split()
        if i[0] == 'A':
            tree.push(int(i[1]))
        elif i[0] == 'B':
            s = Stack()
            for _ in range(tree.size()):
                s.push(tree.pop())
            for _ in range(s.size()):
                item = s.pop()
                if canSee.isEmpty() or canSee.peek() > item:
                    tree.push(item)
                    canSee.push(item)
                elif canSee.peek() < item:
                    while not canSee.isEmpty() and canSee.peek() < item:
                        canSee.pop()
                    canSee.push(item)
                    tree.push(item)
            print(canSee.size())
            canSee = Stack()
        else:
            s = Stack()
            while not tree.isEmpty():
                item = tree.pop()
                s.push(item + 2 if item % 2 == 1 else item - 1)
            while not s.isEmpty():
                tree.push(s.pop())
            