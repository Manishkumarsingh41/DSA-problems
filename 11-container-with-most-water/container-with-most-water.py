class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Current area
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            
            # Update max area
            max_area = max(max_area, area)
            
            # Move pointer with smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
