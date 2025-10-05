class Solution:
    def removeSubstring(self, s, k):
        target = '(' * k + ')' * k
        prev_len = -1
        while len(s) != prev_len:
            prev_len = len(s)
            s = s.replace(target, '')
        return s