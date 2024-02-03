import heapq


class Solution:
    def minCostConnectPoints(self, points):
        def wgt(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        graph = {i: [] for i in range(len(points))}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                weight = wgt(points[i][0], points[i][1], points[j][0], points[j][1])
                graph[i].append((j, weight))
                graph[j].append((i, weight))

        mst = []
        visited = set()
        start_vertex = 0

        min_heap = [(0, start_vertex)]

        while min_heap:
            weight, vertex = heapq.heappop(min_heap)

            if vertex not in visited:
                visited.add(vertex)
                if weight > 0:
                    mst.append(weight)

                for neighbor, edge_weight in graph[vertex]:
                    if neighbor not in visited:
                        heapq.heappush(min_heap, (edge_weight, neighbor))

        return sum(mst)
