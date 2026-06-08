class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""

        start = 0
        max_len = 1

        def expand(l, r, start, max_len):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_len:
                    max_len = r - l + 1
                    start = l
                l -= 1
                r += 1
            return start, max_len

        for i in range(len(s)):
            start, max_len = expand(i, i, start, max_len)       
            start, max_len = expand(i, i + 1, start, max_len)   

        return s[start:start + max_len]
