from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []
        queue = [(0, [0])]

        while queue:
            node, path = queue.pop(0)
            if node == n - 1:
                paths.append(path)
                continue

            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append((neighbor, new_path))

        return paths
