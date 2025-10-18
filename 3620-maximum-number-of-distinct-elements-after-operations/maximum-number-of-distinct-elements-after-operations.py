class Solution:
  def maxDistinctElements(self, nums: list[int], k: int) -> int:
    nums.sort()
    
    distinct_count = 0
    last_val = -float('inf')
    
    for num in nums:
      target = max(num - k, last_val + 1)
      
      if target <= num + k:
        distinct_count += 1
        last_val = target
        
    return distinct_count