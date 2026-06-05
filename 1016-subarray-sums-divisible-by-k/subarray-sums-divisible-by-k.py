class Solution(object):
    def subarraysDivByK(self, nums, k):
        freq = {0: 1}
        prefix = 0
        ans = 0

        for num in nums:
            prefix += num

            rem = prefix % k

            ans += freq.get(rem, 0)

            freq[rem] = freq.get(rem, 0) + 1

        return ans