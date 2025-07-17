class Solution:
    def searchRange(self, nums, target):
        if target not in nums:
            return [-1, -1]

        for i in range(len(nums)):
            if nums[i] == target:
                first = i
                break

        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == target:
                last = j
                break

        return [first, last]
