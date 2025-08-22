class Solution:
    def maxDepth(self, root):
        if not root:
            return 0   # Agar node hi nahi hai to depth 0

        left_depth = self.maxDepth(root.left)   # Left side ki depth nikalenge
        right_depth = self.maxDepth(root.right) # Right side ki depth nikalenge

        return 1 + max(left_depth, right_depth) # Current node ki depth = 1 + max
