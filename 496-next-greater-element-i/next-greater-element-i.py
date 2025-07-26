class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        greater = {}
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                greater[prev] = num
            stack.append(num)
        return [greater.get(num, -1) for num in nums1]
