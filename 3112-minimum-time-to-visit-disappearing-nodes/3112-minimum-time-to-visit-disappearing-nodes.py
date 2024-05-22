class Solution:
    def minimumTime(
        self, n: int, edges: List[List[int]], disappear: List[int]
    ) -> List[int]:
        adjacency_list = {i: [] for i in range(n)}
        for edge in edges:
            u, v, weight = edge
            adjacency_list[u].append((v, weight))
            adjacency_list[v].append((u, weight))

        priority_queue = [(0, 0)]

        answer = [-1] * n
        visited = [False] * n

        heapq.heapify(priority_queue)
        heapq.heappush(priority_queue, (0, 0))
        answer[0] = 0

        while priority_queue:
            current_time, current_node = heapq.heappop(priority_queue)

            if visited[current_node]:
                continue
            visited[current_node] = True

            for neighbor, weight in adjacency_list[current_node]:
                new_time = current_time + weight
                if new_time < disappear[neighbor] and (
                    answer[neighbor] == -1 or new_time < answer[neighbor]
                ):
                    heapq.heappush(priority_queue, (new_time, neighbor))
                    answer[neighbor] = new_time

        return answer
