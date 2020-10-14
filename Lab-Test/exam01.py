class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
 
    def isEmpty(self):
        return self.items == []
 
    def push(self, i):
        self.items.insert(0, i)
 
    def pop(self):
        return self.items.pop(0)
 
    def peek(self):
        return self.items[0]
 
def computePostfix(input_str):
    s = Stack()
    for i in input_str.split():
        if i not in operations:
            s.push(int(i))
        else:
            num1, num2 = s.pop(), s.pop()
            if i == '+':
                s.push(num2+num1)
            elif i == '-':
                s.push(num2-num1)
            elif i == '*':
                s.push(num2*num1)
            elif i == '/':
                s.push(num2/num1)
            elif i == '%':
                s.push(num2%num1)
    return s.pop()

 
 
def postfix_to_bracket_format(input_str):
    numstack = []
 
    for i in input_str.split():
        if i not in operations:
            numstack.append(i)
        else:
            right = numstack.pop()
            left = numstack.pop()
            newresult = " ".join([left, i, right])
            bracket_format = "(" + newresult + ")"
            numstack.append(bracket_format)
    return numstack[0]
 
def postfix_to_infix(input_str):
    s = Stack()
    
    for i in input_str.split():
        if i not in operations:
            s.push(i)
        else:
            num1, num2 = s.pop(), s.pop()
            result = " ".join([num2, i, num1])
            s.push(result)
    return s.pop()
operations = ["+","-","*","/","%"]
s = input('Enter postfix : ')
print("result  --> ", computePostfix(s))
print("infix   --> ", postfix_to_infix(s))
print("bracket --> ", postfix_to_bracket_format(s))
print()
