class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        longest = count = 0
        for value in nums:
            if value == 1:
                count += 1
                longest = max(longest, count)
            else:
                count = 0
        return longest
