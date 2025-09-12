class Solution:
    def doesAliceWin(self, s):
        for ch in s:
            if ch in "aeiou":  # lowercase only since input lowercase
                return True
        return False
