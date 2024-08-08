class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[i].append((i + 1, 1))

        def dijkstra(start: int, end: int, graph: defaultdict[int, List[int]]) -> int:
            distances = {node: float("inf") for node in range(n)}
            distances[start] = 0
            priority_queue = [(0, start)]
            while priority_queue:
                current_distance, current_node = heapq.heappop(priority_queue)
                if current_node == end:
                    return current_distance
                if current_distance > distances[current_node]:
                    continue
                for neighbor, weight in graph[current_node]:
                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(priority_queue, (distance, neighbor))
            return distances[end]

        res = []
        for u, v in queries:
            graph[u].append((v, 1))
            shortest_path = dijkstra(0, n - 1, graph)
            res.append(shortest_path)
        return res
