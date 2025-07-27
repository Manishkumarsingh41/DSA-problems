class Solution(object):
    def maxSubarraySumCircular(self, nums):
        total = sum(nums)
        curr_max = max_sum = nums[0]
        curr_min = min_sum = nums[0]

        for x in nums[1:]:
            curr_max = max(x, curr_max + x)
            max_sum = max(max_sum, curr_max)
            curr_min = min(x, curr_min + x)
            min_sum = min(min_sum, curr_min)

        if max_sum < 0:
            return max_sum
        return max(max_sum, total - min_sum)
