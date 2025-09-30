class Solution(object):
    def triangularSum(self, nums):
        n = len(nums)
        while n > 1:
            nums = [(nums[i] + nums[i+1]) % 10 for i in range(n-1)]
            n -= 1
        return nums[0]
