class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        broken = set(brokenLetters)   # broken letters ko set me daal diya for fast lookup
        words = text.split()          # sentence ko words me tod diya
        count = 0

        for word in words:
            # agar word me koi broken letter nahi hai, tabhi count++
            if all(ch not in broken for ch in word):
                count += 1

        return count
