class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [0] * n
        safe_nodes = []

        def is_safe(node):
            if visited[node] != 0:
                return visited[node] == 2

            visited[node] = 1

            for neighbor in graph[node]:
                if not is_safe(neighbor):
                    return False

            visited[node] = 2

            return True

        for node in range(n):
            if is_safe(node):
                safe_nodes.append(node)

        return safe_nodes
