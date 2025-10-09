class Solution(object):
    def minTime(self, skill, mana):
        acc = [0]
        for x in skill:
            acc.append(acc[-1] + x)
        
        t = 0
        for j in range(1, len(mana)):
            max_val = 0
            for i in range(len(skill)):
                val = mana[j - 1] * acc[i + 1] - mana[j] * acc[i]
                if val > max_val:
                    max_val = val
            t += max_val
        
        return t + acc[-1] * mana[-1]