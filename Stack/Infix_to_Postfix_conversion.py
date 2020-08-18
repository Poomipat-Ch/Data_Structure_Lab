from Stack import *

def convert(inputs):
    s = Stack()
    result = ''
    for i in inputs:
        if i in ('+','-','*','/','(',')'):
            for _ in inputs:
                if i == '(':
                    s.push(i)
                

        else:
            result += i    


