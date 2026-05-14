class Solution:
    def isGood(self, nums: List[int]) -> bool:
        return sorted(nums) == [*range(1,n:=len(nums)),n-1]
        