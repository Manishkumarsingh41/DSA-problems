class Solution(object):
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def dfs(ocean):
            visited = set(ocean)
            stack = list(ocean)
            while stack:
                r, c = stack.pop()
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if (0<=nr<m and 0<=nc<n and (nr,nc) not in visited 
                        and heights[nr][nc] >= heights[r][c]):
                        visited.add((nr,nc))
                        stack.append((nr,nc))
            return visited
        
        pacific = dfs([(i,0) for i in range(m)] + [(0,j) for j in range(n)])
        atlantic = dfs([(i,n-1) for i in range(m)] + [(m-1,j) for j in range(n)])
        
        return [[r,c] for r,c in pacific & atlantic]