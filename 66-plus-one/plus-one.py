class Solution:
    def plusOne(self, digits):
        num = int("".join(map(str, digits)))
        num += 1
        return [int(d) for d in str(num)]
