class Solution:
    def timeRequiredToBuy(self, tickets, k):
        res = tickets[k]
        for i in range(len(tickets)):
            if i < k:
                res += min(tickets[i], tickets[k])
            elif i > k:
                res += min(tickets[i], tickets[k] - 1)
        return res
