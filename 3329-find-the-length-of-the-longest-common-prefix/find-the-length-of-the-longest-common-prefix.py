class Solution:
    def longestCommonPrefix(self, a, b):
        return len(str(max(and_(*({v//10**i for v in e for i in range(9)} for e in (a,b)))) or ''))