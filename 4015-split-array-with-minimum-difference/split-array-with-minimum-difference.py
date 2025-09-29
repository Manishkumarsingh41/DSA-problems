class Solution:
    def splitArray(self, nums):
        n = len(nums)
        inc = [True]*n
        for i in range(1, n):
            inc[i] = inc[i-1] and nums[i] > nums[i-1]

        dec = [True]*n
        for i in range(n-2, -1, -1):
            dec[i] = dec[i+1] and nums[i] > nums[i+1]

        min_diff = float('inf')
        prefix_sum = 0
        for i in range(n-1):
            prefix_sum += nums[i]
            if inc[i] and dec[i+1]:
                min_diff = min(min_diff, abs(prefix_sum - (sum(nums)-prefix_sum)))
        return min_diff if min_diff != float('inf') else -1
