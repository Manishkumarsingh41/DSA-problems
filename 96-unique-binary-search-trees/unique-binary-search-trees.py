class Solution:
    def numTrees(self, n):
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1   # Base case

        for nodes in range(2, n+1):          # 2 se n tak
            for root in range(1, nodes+1):   # Har root try karenge
                dp[nodes] += dp[root-1] * dp[nodes-root]

        return dp[n]
