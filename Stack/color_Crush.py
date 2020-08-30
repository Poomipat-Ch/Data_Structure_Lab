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
    inp = input("Enter Input : ").split()
    s = Stack()
    temp = Stack()
    crush = 0
    i = 0
    finished = False
    while not finished:
        if len(inp) == 0:
            finished = True
        if s.size() > 2:
            s1, s2, s3 = s.pop(), s.pop(), s.pop()
            if s1 == s2 == s3:
                crush += 1
                temp.push(s3)
                temp.push(s2)
                temp.push(s1)
            else:
                s.push(s3)
                s.push(s2)
                s.push(s1)
                if len(inp) > 0:
                    s.push(inp.pop(0))
        else:
            if len(inp) > 0:
                s.push(inp.pop(0))
    
    print(s.size())
    s.item_list.reverse()
    print(''.join(s.item_list) if s.size() > 0 else "Empty")
    if crush > 1:
        print(f"Combo : {crush} ! ! !")