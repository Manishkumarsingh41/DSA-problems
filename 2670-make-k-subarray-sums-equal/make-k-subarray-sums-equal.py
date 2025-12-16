class Solution(object):
    def makeSubKSumEqual(self, arr, k):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(arr)
        g = gcd(n, k)
        ans = 0

        for start in range(g):
            group = []
            i = start

            while True:
                group.append(arr[i])
                i = (i + k) % n
                if i == start:
                    break

            group.sort()
            median = group[len(group) // 2]

            for val in group:
                ans += abs(val - median)

        return ans
