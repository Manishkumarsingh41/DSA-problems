class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        m = 0
        while l < r:
            if height[l] >= height[r]:
                tmp = height[r] * (r - l)
                m = max(m, tmp)
                r -= 1
            else:
                tmp = height[l] * (r - l)
                m = max(m, tmp)
                l += 1
        return m
