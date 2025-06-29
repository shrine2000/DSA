class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))
        
        queue = [(0, k)] # (time, node)
        visited = defaultdict(list)
        while queue:
            time, node = heapq.heappop(queue)
            if node in visited:
                continue
            visited[node] = time
            for ngbr, weight in graph[node]:
                if ngbr not in visited:
                    heapq.heappush(queue, (time + weight, ngbr))
        return max(visited.values()) if len(visited) == n else -1

            


