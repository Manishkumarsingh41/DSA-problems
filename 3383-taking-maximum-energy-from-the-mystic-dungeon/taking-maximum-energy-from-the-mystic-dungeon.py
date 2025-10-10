class Solution(object):
    def maximumEnergy(self, energy, k):
        energy_count = len(energy)
        dp = energy[:]
        for i in range(energy_count - 1 - k, -1, -1):
            dp[i] += dp[i + k]
        return max(dp)
