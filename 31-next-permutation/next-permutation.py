class Solution:
    def nextPermutation(self, nums):
        # Step 1: right se pivot khojna hai (nums[i] < nums[i+1])
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i >= 0:
            # Step 2: pivot ke right me thoda bada element (successor) khojna hai
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]  # swap

        # Step 3: pivot ke baad ke part ko reverse karna hai (minimal banane ke liye)
        l, r = i + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
