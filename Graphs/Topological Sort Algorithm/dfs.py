from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def _dfs(self, v, visited, stack):
        visited[v] = True
        for ngbr in self.graph[v]:
            if not visited[ngbr]:
                self._dfs(ngbr, visited, stack)
        stack.append(v)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        for vertex in range(self.V):
            if not visited[vertex]:
                self._dfs(vertex, visited, stack)
        return stack[::-1]


if __name__ == "__main__":
    graph = Graph(6)
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    print(g.topological_sort())


# Time Complexity: O(V+E)
# Space Complexity: O(V)
