class Solution:
    def rob(self, nums):
        prev2 = 0
        prev1 = 0
        
        for money in nums:
            curr = max(prev1, money + prev2)
            prev2 = prev1
            prev1 = curr
        
        return prev1
