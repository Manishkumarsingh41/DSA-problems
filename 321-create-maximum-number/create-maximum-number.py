class Solution:
    def pick_max(self, nums, t):
        stack = []
        drop = len(nums) - t
        for num in nums:
            while drop and stack and stack[-1] < num:
                stack.pop()
                drop -= 1
            stack.append(num)
        return stack[:t]

    def merge(self, nums1, nums2):
        result = []
        i, j = 0, 0
        while i < len(nums1) or j < len(nums2):
            if nums1[i:] > nums2[j:]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        return result

    def maxNumber(self, nums1, nums2, k):
        max_num = []
        m, n = len(nums1), len(nums2)
        for i in range(max(0, k - n), min(k, m) + 1):
            seq1 = self.pick_max(nums1, i)
            seq2 = self.pick_max(nums2, k - i)
            candidate = self.merge(seq1, seq2)
            if candidate > max_num:
                max_num = candidate
        return max_num
