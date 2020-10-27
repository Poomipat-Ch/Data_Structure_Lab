class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.size = -1

    def insert(self, data, cur_root):
        if cur_root is None:
            return Node(data)
        else:
            self.size += 1
            if cur_root.data == data:
                return cur_root
            elif cur_root.data > data:
                cur_root.left = self.insert(data, cur_root.left)
            else:
                cur_root.right = self.insert(data, cur_root.right)
        return cur_root

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def findMax(self, root):
        if root is None:
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
        if root is None:
            return float('inf') 

        res = root.data
        rres = self.findMin(root.right)
        lres = self.findMin(root.left)

        if rres < res:
            res = rres
        if lres < res:
            res = lres
        return res

    def count_k(self, root, k):
        if root is None:
            return 0

        if root.data <= k:
            return (1 + self.count_k(root.left, k) + self.count_k(root.right, k))
        
        elif root.data > k:
            return self.count_k(root.left, k)

    def preOrder(self, root):
        if root is None:
            return

        print(root.data, end = " ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        if root is None:
            return
        
        self.inOrder(root.left)
        print(root.data,end =" ")
        self.inOrder(root.right)

    def postOrder(self, root):
        if root is None:
            return
        
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, end=' ')


    def breadth(self, root):
        if root is None:
            return
        queue = []
        queue.append(root)
        while len(queue) > 0:
            current = queue.pop(0)
            print(current.data, end=' ')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)






T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
root = Node(inp.pop(0))
for i in inp:
    root = T.insert(i, root)
print('Preorder : ', end='')
T.preOrder(root)
print('\nInorder : ', end='')
T.inOrder(root)
print('\nPostorder : ', end='')
T.postOrder(root)
print('\nBreadth : ', end='')
T.breadth(root)