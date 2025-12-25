class Solution(object):
    def maximumHappinessSum(self, happiness, k):

        happiness.sort(reverse=True)
        
        total = 0
        
        for i in range(k):
            contribution = max(0, happiness[i] - i)
            total += contribution
            
            if contribution == 0:
                break
        
        return total