class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        left , right = 0, len(nums)-1
        average=set()

        while left <right:
            avg=(nums[left]+nums[right])/2
            average.add(avg)
            left+=1
            right-=1

        return len(average)