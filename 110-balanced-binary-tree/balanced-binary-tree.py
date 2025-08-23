class Solution:
    def isBalanced(self, root):
        def check(node):
            if not node:
                return 0   # Empty node ka height 0 hota hai

            # Left subtree ka height nikal
            left = check(node.left)
            if left == -1:   # Agar left unbalanced hai
                return -1

            # Right subtree ka height nikal
            right = check(node.right)
            if right == -1:  # Agar right unbalanced hai
                return -1

            # Agar height difference 1 se zyada ho gaya -> unbalanced
            if abs(left - right) > 1:
                return -1

            # Warna current node ka height return karo
            return max(left, right) + 1

        # Agar -1 aaya matlab unbalanced
        return check(root) != -1
