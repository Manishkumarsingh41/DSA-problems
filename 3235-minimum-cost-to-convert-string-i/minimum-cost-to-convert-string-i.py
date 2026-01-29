class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        from heapq import heappush, heappop
        
        INF = 10**18
        adj = [[] for _ in range(26)]
        
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - 97
            v = ord(c) - 97
            adj[u].append((v, w))
        
        dist = [[INF] * 26 for _ in range(26)]
        
        for src in range(26):
            heap = [(0, src)]
            dist[src][src] = 0
            
            while heap:
                d, u = heappop(heap)
                if d > dist[src][u]:
                    continue
                for v, w in adj[u]:
                    nd = d + w
                    if nd < dist[src][v]:
                        dist[src][v] = nd
                        heappush(heap, (nd, v))
        
        ans = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            u = ord(s) - 97
            v = ord(t) - 97
            if dist[u][v] == INF:
                return -1
            ans += dist[u][v]
        
        return ans
