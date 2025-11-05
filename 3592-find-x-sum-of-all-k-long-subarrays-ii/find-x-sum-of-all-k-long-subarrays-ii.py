from collections import Counter
from sortedcontainers import SortedList

class Solution:
    def findXSum(self, nums, k, x):
        c=Counter();l=SortedList();r=SortedList();S=[0];ans=[]
        def bal():
            while len(l)<x and r:
                f,v=r.pop();l.add((f,v));S[0]+=f*v
            while len(l)>x:
                f,v=l.pop(0);S[0]-=f*v;r.add((f,v))
            while r and l and r[-1]>l[0]:
                f1,v1=r.pop();f2,v2=l.pop(0);S[0]+=f1*v1-f2*v2;l.add((f1,v1));r.add((f2,v2))
        def add(v):
            if c[v]>0:
                p=(c[v],v)
                if p in l:l.remove(p);S[0]-=p[0]*p[1]
                else:r.remove(p)
            c[v]+=1;r.add((c[v],v));bal()
        def rem(v):
            p=(c[v],v)
            if p in l:l.remove(p);S[0]-=p[0]*p[1]
            else:r.remove(p)
            c[v]-=1
            if c[v]>0:r.add((c[v],v))
            bal()
        for i,v in enumerate(nums):
            add(v)
            if i>=k:rem(nums[i-k])
            if i>=k-1:ans.append(S[0])
        return ans
