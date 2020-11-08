class node:
    def __init__(self,value=None):
        self.value=value
        self.left_child=None
        self.right_child=None
        self.parent=None # pointer to parent node in tree
        self.height=1 # height of node in tree (max dist. to leaf) NEW FOR AVL

class AVLTree:
    def __init__(self):
        self.root=None

    def __repr__(self):
        if self.root==None: return ''
        content='\n' # to hold final string
        cur_nodes=[self.root] # all nodes at current level
        cur_height=self.root.height # height of nodes at current level
        sep=' '*(2**(cur_height-1)) # variable sized separator between elements
        while True:
            cur_height+=-1 # decrement current height
            if len(cur_nodes)==0: break
            cur_row=' '
            next_row=''
            next_nodes=[]

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:

                if n==None:
                    cur_row+='   '+sep
                    next_row+='   '+sep
                    next_nodes.extend([None,None])
                    continue

                if n.value!=None:       
                    buf=' '*int((5-len(str(n.value)))/2)
                    cur_row+='%s%s%s'%(buf,str(n.value),buf)+sep
                else:
                    cur_row+=' '*5+sep

                if n.left_child!=None:  
                    next_nodes.append(n.left_child)
                    next_row+=' /'+sep
                else:
                    next_row+='  '+sep
                    next_nodes.append(None)

                if n.right_child!=None: 
                    next_nodes.append(n.right_child)
                    next_row+='\ '+sep
                else:
                    next_row+='  '+sep
                    next_nodes.append(None)

            content+=(cur_height*'   '+cur_row+'\n'+cur_height*'   '+next_row+'\n')
            cur_nodes=next_nodes
            sep=' '*int(len(sep)/2) # cut separator size in half
        return content

    def insert(self,value):
        if self.root==None:
            self.root=node(value)
        else:
            self._insert(value,self.root)

    def _insert(self,value,cur_node):
        if value<cur_node.value:
            if cur_node.left_child==None:
                cur_node.left_child=node(value)
                cur_node.left_child.parent=cur_node # set parent
                self._inspect_insertion(cur_node.left_child)
            else:
                self._insert(value,cur_node.left_child)
        elif value>cur_node.value:
            if cur_node.right_child==None:
                cur_node.right_child=node(value)
                cur_node.right_child.parent=cur_node # set parent
                self._inspect_insertion(cur_node.right_child)
            else:
                self._insert(value,cur_node.right_child)
        else:
            print("Value already in tree!")

    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)

    def _print_tree(self,cur_node):
        if cur_node!=None:
            self._print_tree(cur_node.left_child)
            print ('%s, h=%d'%(str(cur_node.value),cur_node.height))
            self._print_tree(cur_node.right_child)

    def print_inorder(self): 
        print("in_order  --> ",end='')
        if self.root!=None:
            self._print_inorder(self.root)
        print();

    def _print_inorder(self,cur_node):
        if cur_node!=None:
            self._print_inorder(cur_node.left_child)
            print (str(cur_node.value),end=' ')
            self._print_inorder(cur_node.right_child)
            
    def print_preorder(self): 
        print("preorder  --> ",end='')
        if self.root!=None:
            self._print_preorder(self.root)
        print();

    def _print_preorder(self,cur_node):
        if cur_node!=None:
            print (str(cur_node.value),end=' ')
            self._print_preorder(cur_node.left_child)			
            self._print_preorder(cur_node.right_child)
            
    def print_postorder(self): 
        print("postorder --> ",end='')
        if self.root!=None:
            self._print_postorder(self.root)
        print();

    def _print_postorder(self,cur_node):
        if cur_node!=None:
            self._print_postorder(cur_node.left_child)			
            self._print_postorder(cur_node.right_child)
            print (str(cur_node.value),end=' ')
            
    def height(self):
        if self.root!=None:
            return self._height(self.root,0)
        else:
            return 0

    def _height(self,cur_node,cur_height):
        if cur_node==None: return cur_height
        left_height=self._height(cur_node.left_child,cur_height+1)
        right_height=self._height(cur_node.right_child,cur_height+1)
        return max(left_height,right_height)


    # Functions added for AVL...

    def _inspect_insertion(self,cur_node,path=[]):
        if cur_node.parent==None: return
        path=[cur_node]+path

        left_height =self.get_height(cur_node.parent.left_child)
        right_height=self.get_height(cur_node.parent.right_child)

        if abs(left_height-right_height)>1:
            path=[cur_node.parent]+path
            self._rebalance_node(path[0],path[1],path[2])
            return

        new_height=1+cur_node.height 
        if new_height>cur_node.parent.height:
            cur_node.parent.height=new_height

        self._inspect_insertion(cur_node.parent,path)

    def _inspect_deletion(self,cur_node):
        if cur_node==None: return

        left_height =self.get_height(cur_node.left_child)
        right_height=self.get_height(cur_node.right_child)

        if abs(left_height-right_height)>1:
            y=self.taller_child(cur_node)
            x=self.taller_child(y)
            self._rebalance_node(cur_node,y,x)

        self._inspect_deletion(cur_node.parent)

    def _rebalance_node(self,z,y,x):
        if y==z.left_child and x==y.left_child:
            self._right_rotate(z)
        elif y==z.left_child and x==y.right_child:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y==z.right_child and x==y.right_child:
            self._left_rotate(z)
        elif y==z.right_child and x==y.left_child:
            self._right_rotate(y)
            self._left_rotate(z)
        else:
            raise Exception('_rebalance_node: z,y,x node configuration not recognized!')

    def _right_rotate(self,z):
    #     sub_root                    sub_root
    #        |                          |
    #       z                           y
    #      /                             \
    #     /           ==>                 \
    #    y                                 z
    #     \                               /
    #      t3                           t3
        sub_root = z.parent
        y = z.left_child
        t3 = y.right_child
        y.right_child = z
        z.parent = y
        z.left_child = t3
        if t3: t3.parent = z
        y.parent = sub_root
        if y.parent == None:
            self.root = y
        else:
            if y.parent.right_child == z:
                y.parent.right_child = y
            else:
                y.parent.left_child = y
        z.height=1+max(self.get_height(z.left_child),
            self.get_height(z.right_child))
        y.height=1+max(self.get_height(y.left_child),
            self.get_height(y.right_child))

    def _left_rotate(self,z):
    #     sub_root                    sub_root
    #        |                          |
    #       z                           y
    #        \                         /
    #         \           ==>         / 
    #          y                    z
    #         /                      \
    #        t2                       t2
        sub_root=z.parent 
        y=z.right_child
        t2=y.left_child
        y.left_child=z
        z.parent=y
        z.right_child=t2
        if t2!=None: t2.parent=z
        y.parent=sub_root
        if y.parent==None: 
            self.root=y
        else:
            if y.parent.left_child==z:
                y.parent.left_child=y
            else:
                y.parent.right_child=y
        z.height=1+max(self.get_height(z.left_child),
            self.get_height(z.right_child))
        y.height=1+max(self.get_height(y.left_child),
            self.get_height(y.right_child))

    def get_height(self,cur_node):
        if cur_node==None: return 0
        return cur_node.height

    def taller_child(self,cur_node):
        left=self.get_height(cur_node.left_child)
        right=self.get_height(cur_node.right_child)
        return cur_node.left_child if left>=right else cur_node.right_child


print("\n\n *** AVL Tree ***",end='')    
input_string = input("Enter some numbers : ")
bst = AVLTree()
bst.print_tree()
for n in input_string.split():
    bst.insert(int(n))
print()
bst.print_inorder()
bst.print_preorder()
bst.print_postorder()