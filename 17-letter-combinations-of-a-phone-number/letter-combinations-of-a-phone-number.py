class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        keypad = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        result = []

        def backtracking(index, path):
            if index == len(digits):
                result.append(path)
                return

            for letter in keypad[digits[index]]:
                backtracking(index + 1, path + letter)

        backtracking(0, "")
        return result
