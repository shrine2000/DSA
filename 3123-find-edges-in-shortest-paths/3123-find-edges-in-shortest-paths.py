from typing import List
import heapq
from collections import defaultdict


class Solution:
    def findAnswer(self, num_nodes: int, edges: List[List[int]]) -> List[bool]:
        graph = defaultdict(dict)
        for node1, node2, weight in edges:
            graph[node1][node2] = weight
            graph[node2][node1] = weight

        inf = float("inf")

        def dijkstra(source):
            pq = [(0, source)]
            distances = {source: 0}
            while pq:
                dist, curr_node = heapq.heappop(pq)
                if dist != distances[curr_node]:
                    continue

                for neighbor, edge_weight in graph[curr_node].items():
                    neighbor_dist = dist + edge_weight
                    if neighbor_dist < distances.get(neighbor, inf):
                        distances[neighbor] = neighbor_dist
                        heapq.heappush(pq, (neighbor_dist, neighbor))
            return distances

        start_node_distances = dijkstra(0)
        end_node_distances = dijkstra(num_nodes - 1)

        if num_nodes - 1 not in start_node_distances:
            return [False] * len(edges)

        shortest_distance = start_node_distances[num_nodes - 1]
        answers = []

        for node1, node2, weight in edges:
            if (
                start_node_distances.get(node1, inf)
                + weight
                + end_node_distances.get(node2, inf)
                == shortest_distance
                or start_node_distances.get(node2, inf)
                + weight
                + end_node_distances.get(node1, inf)
                == shortest_distance
            ):
                answers.append(True)
            else:
                answers.append(False)

        return answers


if __name__ == "__main__":
    finder = Solution()
    n = 6
    edges = [
        [0, 1, 4],
        [0, 2, 1],
        [1, 3, 2],
        [1, 4, 3],
        [1, 5, 1],
        [2, 3, 1],
        [3, 5, 3],
        [4, 5, 2],
    ]
    print(finder.findAnswer(n, edges))
