class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        total = 1
        for i in range(2, n + 1):
            new_people = 0
            for j in range(max(1, i - forget + 1), max(1, i - delay + 1)):
                new_people = (new_people + dp[j]) % mod
            dp[i] = new_people
            total = (total + new_people) % mod
        ans = 0
        for i in range(max(1, n - forget + 1), n + 1):
            ans = (ans + dp[i]) % mod
        return ans