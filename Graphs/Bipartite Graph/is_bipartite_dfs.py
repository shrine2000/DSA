from typing import List

from collections import deque


def is_bipartite(adj):
    V = len(adj)

    # Using -1, 0, 1 to represent colors
    colors = [-1] * V

    def dfs(vertex, color):
        colors[vertex] = color
        for neighbor in adj[vertex]:
            if colors[neighbor] == -1:
                if not dfs(neighbor, 1 - color):
                    return False
                elif colors[neighbor] == colors[vertex]:
                    return False
        return True

    for i in range(V):
        if colors[i] == -1:
            if not dfs(i, 0):
                return False

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
