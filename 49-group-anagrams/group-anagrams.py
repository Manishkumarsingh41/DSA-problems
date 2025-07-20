class Solution:
    def groupAnagrams(self, A):
        M = {}
        for x in A:
            k = ''.join(sorted(x))
            if k in M:
                M[k].append(x)
            else:
                M[k] = [x]
        return list(M.values())
