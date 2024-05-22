import heapq
from typing import List


# https://leetcode.ca/all/1135.html
# https://www.lintcode.com/problem/3672/


class Solution:
    """
    @param n: the number of cities
    @param connections: the connection info between cities
    @return: minimum cost to connect all cities
    """

    def minimum_cost(self, n: int, connections: List[List[int]]) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for city1, city2, cost in connections:
            graph[city1].append((city2, cost))
            graph[city2].append((city1, cost))

        def prim(graph):
            visited = set()
            pq, mst = [], []
            total_wgt = 0
            start_vertex = next(iter(graph))
            visited.add(start_vertex)

            for ngbr, wgt in graph[start_vertex]:
                heapq.heappush(pq, (wgt, start_vertex, ngbr))
            while pq:
                wgt, u, v = heapq.heappop(pq)
                if v not in visited:
                    mst.append((u, v, wgt))
                    total_wgt += wgt
                    visited.add(v)
                    for ngbr, wgt in graph[v]:
                        if ngbr not in visited:
                            heapq.heappush(pq, (wgt, v, ngbr))
                            visited.add(v)
            return total_wgt if len(visited) == n else -1

        return prim(graph)


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimum_cost(3, [[1, 2, 5], [1, 3, 6], [2, 3, 1]]))  # Output: 6
    print(sol.minimum_cost(4, [[1, 2, 3], [3, 4, 4]]))  # Output: -1
