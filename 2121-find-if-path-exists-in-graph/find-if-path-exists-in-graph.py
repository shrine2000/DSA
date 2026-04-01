class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited =set()

        def dfs(graph, node, visited):
            if node in visited:
                return

            visited.add(node)
            if node == destination:
                return True

            for ngbr in graph[node]:
                if dfs(graph, ngbr, visited):
                    return True

            return False

        return dfs(graph, source, visited)            