class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_end = min_end = max_sum = min_sum = 0  
        for num in nums:
            max_end = max(num, max_end + num)
            min_end = min(num, min_end + num)

            max_sum = max(max_sum, max_end)
            min_sum = min(min_sum, min_end)

        return max(max_sum, -min_sum)