class Solution:
    def rotateGrid(self, grid, k):

        m, n = len(grid), len(grid[0])

        for layer in range(min(m, n) // 2):

            top = left = layer
            bottom = m - layer - 1
            right = n - layer - 1

            arr = []

            for j in range(left, right + 1):
                arr.append(grid[top][j])

            for i in range(top + 1, bottom):
                arr.append(grid[i][right])

            for j in range(right, left - 1, -1):
                arr.append(grid[bottom][j])

            for i in range(bottom - 1, top, -1):
                arr.append(grid[i][left])

            rot = k % len(arr)
            arr = arr[rot:] + arr[:rot]

            idx = 0

            for j in range(left, right + 1):
                grid[top][j] = arr[idx]
                idx += 1

            for i in range(top + 1, bottom):
                grid[i][right] = arr[idx]
                idx += 1

            for j in range(right, left - 1, -1):
                grid[bottom][j] = arr[idx]
                idx += 1

            for i in range(bottom - 1, top, -1):
                grid[i][left] = arr[idx]
                idx += 1

        return grid