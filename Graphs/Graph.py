from collections import deque
from typing import List, Dict, Set


class Graph:
    def __init__(self) -> None:
        self.adj_list: Dict[int, List[int]] = {}

    def add_edge(self, u: int, v: int) -> None:
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)

    def bfs(self, start: int) -> List[int]:
        visited: Set[int] = set()
        queue: deque = deque([start])
        visited.add(start)
        traversal_path: List[int] = []

        while queue:
            node: int = queue.popleft()
            traversal_path.append(node)

            if node in self.adj_list:
                for neighbor in self.adj_list[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        return traversal_path

    def dfs(self, start: int) -> List[int]:
        visited: Set[int] = set()
        traversal_path: List[int] = []

        def dfs_util(node: int) -> None:
            visited.add(node)
            traversal_path.append(node)

            if node in self.adj_list:
                for neighbor in self.adj_list[node]:
                    if neighbor not in visited:
                        dfs_util(neighbor)

        dfs_util(start)
        return traversal_path


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    start_node = 2
    bfs_traversal = graph.bfs(start_node)
    dfs_traversal = graph.dfs(start_node)

    print("BFS Traversal from node", start_node, ":", bfs_traversal)
    print("DFS Traversal from node", start_node, ":", dfs_traversal)
