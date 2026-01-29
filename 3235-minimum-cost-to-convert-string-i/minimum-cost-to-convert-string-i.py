class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        INF = 10**18
        dist = [[INF]*26 for _ in range(26)]
        
        for i in range(26):
            dist[i][i] = 0
        
        for o, c, w in zip(original, changed, cost):
            x = ord(o) - 97
            y = ord(c) - 97
            dist[x][y] = min(dist[x][y], w)
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        ans = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            x = ord(s) - 97
            y = ord(t) - 97
            if dist[x][y] == INF:
                return -1
            ans += dist[x][y]
        
        return ans
