class Solution:
    def recoverTree(self, root):
        # Galat nodes track karne ke liye
        self.first = None
        self.second = None
        self.prev = None

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            # Check for inversion: jab prev > current
            if self.prev and self.prev.val > node.val:
                # First inversion: set first
                if not self.first:
                    self.first = self.prev
                # Second node is current (update always)
                self.second = node

            self.prev = node  # update prev now
            inorder(node.right)

        inorder(root)
        # Swap the values to fix BST
        self.first.val, self.second.val = self.second.val, self.first.val