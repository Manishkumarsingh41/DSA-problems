class Solution:
    def isBalanced(self, root):
        
        def dfs(node):
            if not node:
                return 0  # Empty tree ka height 0

            left = dfs(node.left)   # Left subtree ka height
            right = dfs(node.right) # Right subtree ka height

            # Agar koi side unbalanced tha
            if left == -1 or right == -1:
                return -1

            # Agar difference 1 se zyada hai
            if abs(left - right) > 1:
                return -1

            # Warna is node ka height
            return 1 + max(left, right)

        return dfs(root) != -1
