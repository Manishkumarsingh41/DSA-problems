class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        word = sentence.split()
        for i,word in enumerate(word):
            if word.startswith(searchWord):
                return i+1
        return -1
        