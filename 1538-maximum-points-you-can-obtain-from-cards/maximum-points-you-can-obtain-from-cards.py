class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        current = sum(cardPoints[:k])
        max_score = current
        for i in range(k):
            current -= cardPoints[k - 1 - i]
            current += cardPoints[-1 - i]
            max_score = max(max_score, current)
        return max_score
