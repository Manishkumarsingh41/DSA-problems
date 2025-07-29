class Solution:
    def isMatch(self, text, pattern):
        rows = len(text)
        cols = len(pattern)
        match = [[False] * (cols + 1) for _ in range(rows + 1)]
        match[0][0] = True

        for j in range(2, cols + 1):
            if pattern[j - 1] == "*":
                match[0][j] = match[0][j - 2]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if pattern[j - 1] == text[i - 1] or pattern[j - 1] == ".":
                    match[i][j] = match[i - 1][j - 1]
                elif pattern[j - 1] == "*":
                    match[i][j] = match[i][j - 2]
                    if pattern[j - 2] == text[i - 1] or pattern[j - 2] == ".":
                        match[i][j] = match[i][j] or match[i - 1][j]

        return match[rows][cols]
