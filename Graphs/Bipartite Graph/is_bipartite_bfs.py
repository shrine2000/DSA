from typing import List

from collections import deque


def is_bipartite(adj):
    V = len(adj)

    colors = [-1] * V # Initialize colors for nodes: -1 for uncolored, 0 and 1 for two colors

    for i in range(V):
        if colors[i] == -1:
            colors[i] = 0
            queue = deque([i])

            while queue:
                u = queue.popleft()

                for v in adj[u]:
                    if colors[v] == colors[u]:
                        return False

                    if colors[v] == -1:
                        colors[v] = 1 - colors[u]
                        queue.append(v)
    return True


if __name__ == "__main__":

    adjacency_list = [
        [1, 3],
        [0, 2],
        [1, 3],
        [0, 2]
    ]

    result = is_bipartite(adjacency_list)
    if result:
        print("The graph is bipartite.")
    else:
        print("The graph is not bipartite.")
