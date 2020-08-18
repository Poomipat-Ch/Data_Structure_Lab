from Stack import * 


def posfix(inputs):
    s = Stack()
    for i in inputs:
        if type(i) == int:
            s.push(i)
        else:
            if i in ('+','-','*','/'):
                op1, op2 = s.pop(), s.pop()
                if i == '+':
                       s.push(op1+op2)
                elif i == '-':
                    s.push(op2-op1)
                elif i == '*':
                    s.push(op1 * op2)
                elif i == '/':
                    s.push(op2 / op1)
    return s.pop()
print(posfix((1,2,3,'+','*')))