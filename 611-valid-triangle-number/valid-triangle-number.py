class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        n, count = len(nums), 0
        for i in range(n - 1, 1, -1):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    count += r - l
                    r -= 1
                else:
                    l += 1
        return count
