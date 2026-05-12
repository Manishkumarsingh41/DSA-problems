class Solution:
    def minimumEffort(self, tasks):

        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)

        current = 0
        extra = 0

        for actual, minimum in tasks:

            if current < minimum:

                extra += (minimum - current)

                current = minimum

            current -= actual

        return extra