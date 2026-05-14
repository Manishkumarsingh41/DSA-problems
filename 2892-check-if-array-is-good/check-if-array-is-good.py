class Solution:
    def isGood(self, nums: List[int]) -> bool:
        return sum(nums) == -~ (n:= len(nums))*n//2-1 and n-1==len({*nums})== max(nums)
        