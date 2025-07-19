class Solution:
    def subsets(self, nums):
        n = len(nums)
        res = []
        for mask in range(1 << n):
            subset = []
            for j in range(n):
                if mask & (1 << j):
                    subset.append(nums[j])
            res.append(subset)
        return res
