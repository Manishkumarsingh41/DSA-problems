class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        n = len(nums)
        right = [1]*n
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                right[i]=right[i+1]+1
        def ok(k):
            for i in range(n-2*k+1):
                if right[i]>=k and right[i+k]>=k:
                    return True
            return False
        l,r=0,n//2
        while l<r:
            m=(l+r+1)//2
            if ok(m): l=m
            else: r=m-1
        return l
