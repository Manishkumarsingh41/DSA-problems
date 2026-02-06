class Solution:
    def maxFrequency(self, nums, k):
        nums.sort()
        l = 0
        total = 0
        ans = 0

        for r in range(len(nums)):
            total += nums[r]
            while nums[r] * (r - l + 1) - total > k:
                total -= nums[l]
                l += 1
            ans = max(ans, r - l + 1)

        return ans
