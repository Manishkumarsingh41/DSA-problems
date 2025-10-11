class Solution:
    def maximumTotalDamage(self, power):
        freq = {}
        for x in power:
            freq[x] = freq.get(x, 0) + 1
        s = sorted(freq)
        dp = []
        p = 0
        for i, x in enumerate(s):
            gain = x * freq[x]
            if not dp:
                dp.append(gain)
                continue
            while p < i and s[p] < x - 2:
                p += 1
            take = gain + (dp[p - 1] if p - 1 >= 0 else 0)
            dp.append(take if take > dp[-1] else dp[-1])
        return dp[-1]
