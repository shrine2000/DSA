class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n

        for i in range(n):
            if colors[i] == -1:
                queue = deque([i])
                colors[i] = 0

                while queue:
                    node = queue.popleft()

                    for ngbr in graph[node]:
                        if colors[ngbr] == -1:
                            colors[ngbr] = 1 - colors[node]
                            queue.append(ngbr)
                        elif colors[ngbr] == colors[node]:
                            return False

        return True
