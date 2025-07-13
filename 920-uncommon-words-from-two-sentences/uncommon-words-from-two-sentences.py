class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        d = {}
        for ch in s1.split() + s2.split():
            d[ch] = d.get(ch, 0) + 1
        return [ch for ch in d if d[ch] == 1]
