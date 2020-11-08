if balance > 1 and data >= cur_root.left.data:
            cur_root.left = self.leftRotate(cur_root.left)
            return self.rightRotate(cur_root)