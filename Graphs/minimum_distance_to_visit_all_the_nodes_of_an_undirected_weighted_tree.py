from typing import List


# https://www.geeksforgeeks.org/minimum-distance-to-visit-all-the-nodes-of-an-undirected-weighted-tree/


# Given a weighted tree with N nodes starting from 1 to N.
# The distance between any two nodes is given by the edge weight.
# Node 1 is the source, the task is to visit all the nodes of the tree with the minimum distance traveled.


class Edge:
    def __init__(self, src, dest, weight):
        self.source = src
        self.destination = dest
        self.weight = weight


def add_edge(adj_list, source, destination, weight):
    adj_list[source].append(Edge(source, destination, weight))
    adj_list[destination].append(Edge(destination, source, weight))


def dfs_compute_distances(adj_list, distances, node, parent, current_distance, visited):
    distances[node] = current_distance
    visited[node] = True

    for edge in adj_list[node]:
        if not visited[edge.destination]:
            dfs_compute_distances(
                adj_list,
                distances,
                edge.destination,
                node,
                current_distance + edge.weight,
                visited,
            )


if __name__ == "__main__":
    num_nodes = 6
    adjacency_list = [[] for _ in range(num_nodes)]
    distances = [-1] * num_nodes
    visited = [False] * num_nodes
    total_weight = 0

    sources = [2, 3, 5, 6, 4]
    destinations = [1, 1, 2, 2, 1]
    weights = [1, 4, 2, 50, 5]

    for i in range(num_nodes - 1):
        total_weight += 2 * weights[i]
        add_edge(adjacency_list, destinations[i] - 1, sources[i] - 1, weights[i])

    dfs_compute_distances(adjacency_list, distances, 0, -1, 0, visited)
    max_distance_from_root = max(distances[1:])
    min_distance_traveled = total_weight - max_distance_from_root

    print(min_distance_traveled)
