class Solution:
    def earliestTime(self, tasks: list[list]):
        return min([start + duration for start, duration in tasks])