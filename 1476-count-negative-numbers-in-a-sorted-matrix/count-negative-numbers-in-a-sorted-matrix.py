class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        neg_cnt = 0
        for block in range(m):
            for i in range(n-1,-1,-1):
                if grid[block][i] < 0:
                    neg_cnt += 1
                else:
                    break
        return neg_cnt