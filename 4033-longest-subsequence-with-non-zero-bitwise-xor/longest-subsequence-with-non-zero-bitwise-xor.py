class Solution:
    def longestSubsequence(self, nums):
        n = len(nums)
        total_xor = 0
        for num in nums:
            total_xor ^= num
        
        if total_xor != 0:
            return n
        
        if all(num == 0 for num in nums):
            return 0
        
        for i in range(n):
            if nums[i] != 0:
                return n - 1
        
        return 0