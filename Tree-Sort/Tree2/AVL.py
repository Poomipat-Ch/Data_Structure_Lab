class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1   
    
    def __str__(self):
        return str(self.data)

class AVL:

    def insert(self, data, cur_root):
        if cur_root is None:
            return Node(data) 
        elif cur_root.data > data:
            cur_root.left = self.insert(data, cur_root.left)
        else:
            cur_root.right = self.insert(data, cur_root.right)
        
        cur_root.height = 1 + max(self.get_height(cur_root.left), self.get_height(cur_root.right))
        balance = self.get_balance(cur_root)
        if balance > 1 and data < cur_root.left.data:
            return self.rightRotate(cur_root)
        if balance < -1 and data >= cur_root.right.data:
            return self.leftRotate(cur_root)
        if balance > 1 and data >= cur_root.left.data:
            cur_root.left = self.leftRotate(cur_root.left)
            return self.rightRotate(cur_root)
        if balance < -1 and data < cur_root.right.data:
            cur_root.right = self.rightRotate(cur_root.right)
            return self.leftRotate(cur_root)
        return cur_root

    def leftRotate(self, node):
        y = node.right
        x = y.left

        y.left = node
        node.right = x

        node.height = 1+max(self.get_height(node.left),self.get_height(node.right))
        y.height = 1+max(self.get_height(y.left),self.get_height(y.right))

        return y

    def rightRotate(self, node):
        y = node.left
        x = y.right

        y.right = node
        node.left = x

        node.height = 1+max(self.get_height(node.left),self.get_height(node.right))
        y.height = 1+max(self.get_height(y.left),self.get_height(y.right))
        
        return y

    def get_height(self, root):
        if root is None:
            return 0
        return root.height

    def get_balance(self, root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = AVL()
inp = [int(i) for i in input('Enter Input : ').split()]
root = None
for i in inp:
    print(f'Insert : ( {i} )')
    root = T.insert(i, root)
    T.printTree(root)
    print('--------------------------------------------------')
