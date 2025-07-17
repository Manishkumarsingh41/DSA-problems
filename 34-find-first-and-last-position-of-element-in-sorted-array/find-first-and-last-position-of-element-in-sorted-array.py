class Solution(object):
    def searchRange(self, nums, target):
        start = -1
        end = -1

        for i in range(len(nums)):
            if nums[i] == target and start == -1:
                start = i

        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                end = j
                break

        return [start, end]
