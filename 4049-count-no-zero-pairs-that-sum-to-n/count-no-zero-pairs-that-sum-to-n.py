class Solution(object):
    def countNoZeroPairs(self, n):
        nd = list(map(int, str(n)))[::-1]
        m  = len(nd)
        memo = {}
        def dfs(p, carry, la, lb):
            key = (p, carry, la, lb)
            if key in memo:
                return memo[key]
            if p == m:
                return int(carry == 0)
            rng_a = range(1,10) if p < la else (0,)
            rng_b = range(1,10) if p < lb else (0,)
            ways  = 0
            for da in rng_a:
                for db in rng_b:
                    s = da + db + carry
                    if s % 10 == nd[p]:
                        ways += dfs(p + 1, s // 10, la, lb)
            memo[key] = ways
            return ways
        return sum(dfs(0, 0, la, lb) for la in range(1, m + 1) for lb in range(1, m + 1))