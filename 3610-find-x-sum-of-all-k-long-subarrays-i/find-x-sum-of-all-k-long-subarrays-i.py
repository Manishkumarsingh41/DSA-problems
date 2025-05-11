from typing import List
from collections import Counter
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        freq = Counter(nums[:k])
        for i in range(len(nums) - k + 1):
            top = sorted(freq.items(), key=lambda t: (-t[1], -t[0]))[:x]
            res.append(sum(n * freq[n] for n, _ in top))
            if i + k < len(nums):
                out_num, in_num = nums[i], nums[i + k]
                freq[out_num] -= 1
                if freq[out_num] == 0:
                    del freq[out_num]
                freq[in_num] += 1
        
        return res
