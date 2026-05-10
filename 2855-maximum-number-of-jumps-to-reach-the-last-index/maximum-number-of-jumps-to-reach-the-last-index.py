class Solution(object):
    def maximumJumps(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        dp = {}

        def f(i, n=len(nums)):

            if i == n - 1:
                return 0

            if i in dp:
                return dp[i]

            res = float('-inf')

            for j in range(i + 1, n):

                if abs(nums[i] - nums[j]) <= target:
                    res = max(res, 1 + f(j))

            dp[i] = res

            return res

        return max(f(0), -1)