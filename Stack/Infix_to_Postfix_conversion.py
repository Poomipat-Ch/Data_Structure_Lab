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


def infixToPostfix(infixexpr):
    prec = {"^":4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    opStack = Stack()
    postfixList = ''

    for token in infixexpr:
        if (token >= 'a' and token <= 'z') or (token >= 'A' and token <= 'Z'):
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

if __name__ == "__main__":
    n = input('Enter Infix : ')
    print('Postfix :',infixToPostfix(n))

            
