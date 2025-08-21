class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')  # Global best sum (answer store karne ke liye)
        
        def dfs(node):
            if not node:
                return 0  # Null node ka contribution 0 hoga
            
            # Left aur right subtree se best gain nikalenge (negative ho to ignore)
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            
            # Current node ke through ek full path banega (left + right + node)
            current_sum = node.val + left_gain + right_gain
            
            # Global max update karenge agar yaha ka path better hai
            self.max_sum = max(self.max_sum, current_sum)
            
            # Parent ko return hamesha ek side ka best gain hi karenge
            return node.val + max(left_gain, right_gain)
        
        dfs(root)  # DFS call
        return self.max_sum  # Final answer
