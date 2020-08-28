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

def match(open, close):
    return(open == '(' and close == ')') or (open == '[' and close == ']')

def checkParentheses(s):
    st = Stack()
    i = 0
    error = 0
    while i < len(s) and error == 0:
        c = s[i]
        if c in '([':
            st.push(c)
        elif c in ')]':
            if st.size() > 0:
                if not match(st.pop(),c):
                    error = 1
            else:
                error = 2
        i += 1
    if st.size() > 0:
        error = 3
    
    return "Matched ! ! !" if error == 0 else "Unmatched ! ! !"

if __name__ == "__main__":
    s = input('Enter Input : ')
    print("Parentheses :",checkParentheses(s))