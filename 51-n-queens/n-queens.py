class Solution:
    def solveNQueens(self, n):
        res = []
        board = [["."]*n for _ in range(n)]
        cols, diag1, diag2 = set(), set(), set()  # track columns and diagonals

        def backtrack(row):
            if row == n:  # sab queens place ho gaye
                res.append(["".join(r) for r in board])
                return
            for col in range(n):
                if col in cols or (row+col) in diag1 or (row-col) in diag2:
                    continue  # yaha queen nahi rakh sakte
                # queen place karo
                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row+col)
                diag2.add(row-col)
                backtrack(row+1)  # next row
                # backtrack -> queen hata do
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row+col)
                diag2.remove(row-col)

        backtrack(0)
        return res
