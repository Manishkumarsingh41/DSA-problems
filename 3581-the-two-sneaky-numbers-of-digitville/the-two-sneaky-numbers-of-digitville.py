class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set()
        result = []
        
        for num in nums:
            if num in seen:
                result.append(num)
            else:
                seen.add(num)
        
        return result