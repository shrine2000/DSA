class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        mincycle = float('inf')
        for i in range(n):
            dist = [-1] * n
            queue = deque()
            queue.append(i)
            dist[i] = 0
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        queue.append(v)
                    elif v != i and dist[v] >= dist[u]:
                        mincycle = min(mincycle, dist[u] + dist[v] + 1)
                        
        return -1 if mincycle == float('inf') else mincycle
        