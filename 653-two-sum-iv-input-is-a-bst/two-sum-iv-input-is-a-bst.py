class Solution:
    def findTarget(self, root, k):
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        
        nums = inorder(root)
        left, right = 0, len(nums) - 1
        
        while left < right:
            total = nums[left] + nums[right]
            if total == k:
                return True
            elif total < k:
                left += 1
            else:
                right -= 1
        return False
