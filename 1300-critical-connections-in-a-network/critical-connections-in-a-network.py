class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        disc = [0] * n
        low = [0] * n
        time = [1]
        bridges = []

        def dfs(u, parent):
            disc[u] = low[u] = time[0]
            time[0] += 1
            for v in graph[u]:
                if v == parent:
                    continue
                if disc[v] == 0:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        bridges.append([u, v])
                else:
                    low[u] = min(low[u], disc[v])
        
        for i in range(n):
            if disc[i] == 0:
                dfs(i, -1)
        
        return bridges
