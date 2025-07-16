class Solution(object):
    def isSameAfterReversals(self, num):
        return num == int(str(int(str(num)[::-1]))[::-1])
