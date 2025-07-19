class Solution(object):
    def sortedArrayToBST(self, nums):
        def dfs(l, r):
            if l > r: return None
            m = (r + l) // 2
            node = TreeNode(nums[m])
            node.left = dfs(l, m - 1)
            node.right = dfs(m + 1, r)
            return node
        return dfs(0, len(nums) - 1)
