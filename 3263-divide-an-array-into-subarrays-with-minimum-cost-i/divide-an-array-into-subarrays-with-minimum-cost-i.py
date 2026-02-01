class Solution:
    def minimumCost(self, a):
        return a[0]+sum(sorted(a[1:])[:2])