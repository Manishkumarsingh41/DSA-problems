class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        odd_count = 0
        prefix = {0: 1}
        
        for num in nums:
            if num % 2:
                odd_count += 1
            count += prefix.get(odd_count - k, 0)
            prefix[odd_count] = prefix.get(odd_count, 0) + 1
            
        return count
