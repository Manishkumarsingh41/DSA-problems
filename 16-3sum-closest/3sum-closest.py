class Solution:
    def threeSumClosest(self, nums, target):
        closest_sum = float('inf')
        nums.sort()

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                difference = total - target

                if abs(difference) < abs(closest_sum - target):
                    closest_sum = total

                if difference < 0:
                    left += 1
                elif difference > 0:
                    right -= 1
                else:
                    return closest_sum

        return closest_sum
