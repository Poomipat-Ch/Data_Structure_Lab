from Stack import *

def infixToPostfix(infixexpr):
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    opStack = Stack()
    postfixList = ''

    for token in infixexpr:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList += token
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList += topToken
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList += opStack.pop()
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList += opStack.pop()
    return postfixList

print(infixToPostfix("10+3*5/(16-4)"))
print(infixToPostfix("(A+B)*C-(D-E)*(F+G)"))
            
