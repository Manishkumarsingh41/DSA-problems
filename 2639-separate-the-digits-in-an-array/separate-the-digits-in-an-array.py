class Solution:
    def separateDigits(self, nums):

        result = []

        for num in nums:

            s = str(num)

            for ch in s:

                result.append(int(ch))

        return result