class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        cycle_length = [-1] * len(edges)
        visited = [False] * len(edges)
        max_length = -1

        for i in range(len(edges)):
            if not visited[i]:
                visited[i] = True
                next_node = edges[i]
                length = 1
                node_to_distance = {i: 0}

                while next_node != -1 and not visited[next_node]:
                    node_to_distance[next_node] = length
                    visited[next_node] = True
                    next_node = edges[next_node]
                    length += 1

                if next_node != -1 and next_node in node_to_distance:
                    cycle_length[next_node] = length - node_to_distance[next_node]
                    max_length = max(max_length, length - node_to_distance[next_node])

        return max_length
