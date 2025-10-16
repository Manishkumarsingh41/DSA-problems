class Solution:
    def findSmallestInteger(self, nums, value):
        from collections import Counter
        c = Counter(x % value for x in nums)
        for i in range(len(nums)+1):
            if c[i % value] == 0:
                return i
            c[i % value] -= 1
