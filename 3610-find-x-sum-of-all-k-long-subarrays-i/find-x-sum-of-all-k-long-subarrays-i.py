class Solution(object):
    def findXSum(self, nums, k, x):
        n=len(nums);ans=[]
        for i in range(n-k+1):
            c={}
            for v in nums[i:i+k]:c[v]=c.get(v,0)+1
            s=sorted(c.items(),key=lambda a:(-a[1],-a[0]))
            top={a for a,_ in s[:x]}
            ans.append(sum(v for v in nums[i:i+k] if v in top))
        return ans
