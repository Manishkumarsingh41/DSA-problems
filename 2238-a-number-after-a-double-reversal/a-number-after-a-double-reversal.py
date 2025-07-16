class Solution:
    def reverseInteger(self, n):
        sign = -1 if n < 0 else 1
        rev = int(str(abs(n))[::-1])
        result = sign * rev
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result

    def isSameAfterReversals(self, num):
        r = self.reverseInteger(num)
        rr = self.reverseInteger(r)
        return rr == num
