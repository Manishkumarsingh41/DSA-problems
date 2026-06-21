class Solution:
    def maxIceCream(self, costs, coins):
        freq = [0] * (max(costs) + 1)

        for c in costs:
            freq[c] += 1

        ans = 0

        for price in range(1, len(freq)):
            if freq[price]:
                buy = min(freq[price], coins // price)
                ans += buy
                coins -= buy * price

        return ans