from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n, edges) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node: int):
            visited.add(node)
            for ngbr in graph[node]:
                if ngbr not in visited:
                    dfs(ngbr)

        count = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        return count


# tc - O(n + e)
# sc - o(n + e)
