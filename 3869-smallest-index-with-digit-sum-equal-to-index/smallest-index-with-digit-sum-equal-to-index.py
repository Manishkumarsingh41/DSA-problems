class Solution:
    def smallestIndex(self, a: List[int]) -> int:
        return next((i for i,v in enumerate(a) if sum(map(int,str(v)))==i),-1)