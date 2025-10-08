class Solution:
    def successfulPairs(self, spells, potions, success):
        n = len(spells)
        m = len(potions)
        potions.sort()
        spells_with_idx = sorted([(s, i) for i, s in enumerate(spells)]) 
        
        res = [0] * n
        j = m - 1
        
        for s, idx in spells_with_idx:
            while j >= 0 and s * potions[j] >= success:
                j -= 1
            res[idx] = m - (j + 1)
        
        return res
