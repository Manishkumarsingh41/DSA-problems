class Solution(object):
    def mostBooked(self, n, meetings):
        meetings.sort()
        ans = [0] * n
        times = [0] * n

        for start, end in meetings:
            free = -1
            earliest = 0

            for i in range(n):
                if times[i] <= start:
                    free = i
                    break
                if times[i] < times[earliest]:
                    earliest = i

            if free != -1:
                ans[free] += 1
                times[free] = end
            else:
                ans[earliest] += 1
                times[earliest] += end - start

        return max(range(n), key=lambda i: ans[i])
