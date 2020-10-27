class Node:
    def __init__(self,data,left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.data)



class BST:
    def insert(self, data, cur_root):
        if cur_root is None:
            print('*',end="")
            return Node(data)
        else:
            if cur_root.data == data:
                return cur_root
            elif cur_root.data > data:
                print('L',end="")
                cur_root.left = self.insert(data, cur_root.left)
            else:
                print('R',end="")
                cur_root.right = self.insert(data, cur_root.right)
        return cur_root

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
root = None
for i in inp:
    root = T.insert(i, root)
    print()
