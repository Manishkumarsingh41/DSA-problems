class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if nums[j] == 0 and nums[j+1] != 0:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if not swapped:  # Agar koi swap nahi hua, toh break karo
                break
