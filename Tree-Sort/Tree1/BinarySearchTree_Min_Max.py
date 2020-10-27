class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data, root):
        if root is None:
            return Node(data)
        else:
            if root.data == data:
                return root
            elif root.data > data:
                root.left = self.insert(data, root.left)
            else:
                root.right = self.insert(data, root.right)
        return root
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def findMax(self, root):
        if root == None:
            return float('-inf')

        res = root.data
        lres = self.findMax(root.left)
        rres = self.findMax(root.right)

        if lres > res:
            res = lres
        if rres > res:
            res = rres
        return res

    def findMin(self, root):
        if root == None:
            return float('inf') 

        res = root.data
        rres = self.findMin(root.right)
        lres = self.findMin(root.left)

        if rres < res:
            res = rres
        if lres < res:
            res = lres
        return res

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
root = Node(inp.pop(0))
for i in inp:
    root = T.insert(i, root)
T.printTree(root)
print('--------------------------------------------------')
print("Min :",T.findMin(root))
print("Max :",T.findMax(root))