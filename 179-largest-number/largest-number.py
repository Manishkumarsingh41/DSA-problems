class Solution(object):
    def largestNumber(self, nums):
        nums = list(map(str, nums))
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        result = ''.join(nums)
        return '0' if result[0] == '0' else result
