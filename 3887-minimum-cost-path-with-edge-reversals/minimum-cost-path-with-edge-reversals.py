import heapq

class Solution:
    def minCost(self, n, edges):
        adj = [[] for _ in range(n)]
        
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, 2 * w))
        
        dist = [10**18] * n
        dist[0] = 0
        
        heap = [(0, 0)]
        
        while heap:
            d, u = heapq.heappop(heap)
            
            if d > dist[u]:
                continue
            
            if u == n - 1:
                return d
            
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))
        
        return -1
