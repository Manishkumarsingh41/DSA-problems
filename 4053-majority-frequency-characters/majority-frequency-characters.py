class Solution:
    def majorityFrequencyGroup(self, s):
        f = {}
        for c in s:
            f[c] = f.get(c, 0) + 1
        g = {}
        for c, v in f.items():
            g[v] = g.get(v, []) + [c]
        k = max(g, key=lambda x: (len(g[x]), x))
        return ''.join(g[k])
