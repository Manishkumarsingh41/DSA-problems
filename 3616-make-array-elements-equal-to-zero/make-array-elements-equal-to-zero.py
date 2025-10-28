class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, ans = len(nums), 0

        def can_zero(start, d):
            arr, i = nums[:], start
            while 0 <= i < n:
                if arr[i] == 0:
                    i += d
                else:
                    arr[i] -= 1
                    d = -d
                    i += d
            return all(x == 0 for x in arr)

        for i, x in enumerate(nums):
            if x == 0:
                ans += can_zero(i, 1) + can_zero(i, -1)
        return ans
