class Solution(object):
    def maxSubArray(self, nums):
        max_sum=nums[0]
        current_sum=0
        for i in nums:
            if current_sum <0:
                current_sum=0
            current_sum+=i
            if current_sum > max_sum:
                max_sum =current_sum
        return max_sum