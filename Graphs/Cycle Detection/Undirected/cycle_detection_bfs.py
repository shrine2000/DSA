from collections import defaultdict, deque
from typing import DefaultDict, List, Dict


class Graph:
    def __init__(self) -> None:
        self.graph: DefaultDict[int, List[int]] = defaultdict(list)

    def add_edge(self, u: int, v: int) -> None:
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_cyclic_util(
        self, v: int, visited: Dict[int, bool], parent: Dict[int, int]
    ) -> bool:
        queue: deque = deque()
        queue.append(v)
        visited[v] = True

        while queue:
            current: int = queue.popleft()
            for neighbor in self.graph[current]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    parent[neighbor] = current
                elif parent[current] != neighbor:
                    return True

        return False

    def is_cyclic(self) -> bool:
        visited: Dict[int, bool] = {node: False for node in self.graph}
        parent: Dict[int, int] = {node: -1 for node in self.graph}

        for node in self.graph:
            if not visited[node]:
                if self.is_cyclic_util(node, visited, parent):
                    return True

        return False


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    if g.is_cyclic():
        print("Graph contains a cycle")
    else:
        print("Graph doesn't contain a cycle")
