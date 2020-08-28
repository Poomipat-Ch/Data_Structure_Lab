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


def posfix(inputs):
    s = Stack()
    for i in inputs:
        if type(i) == int or i in ('DUP','POP','PSH'):
            if type(i) == int:
                s.push(i)
            elif i == 'DUP':
                s.push(s.peek())
            elif i == 'POP':
                s.pop()
            #elif 'PSH':
        elif i in ('+','-','*','/'):
                op1, op2 = s.pop(), s.pop()
                if i == '+':
                       s.push(op1+op2)
                elif i == '-':
                    s.push(op1-op2)
                elif i == '*':
                    s.push(op1 * op2)
                elif i == '/':
                    s.push(op1 / op2)
        else:
            return 'Invalid instruction: '+i
            
    return int(s.pop()) if not s.isEmpty() else 0
if __name__ == "__main__":
    s = input('* Stack Calculator *\nEnter arguments : ').split()
    x = []
    for i in s:
        if i >= '0' and i <= '9':
            x.append(int(i))
        else:
            x.append(i)
    print(posfix(x))
