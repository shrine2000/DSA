# https://www.youtube.com/watch?v=lfJlCla-X8Y&ab_channel=AryanMittal

class Solution:
    def dfs(self, node, parent, dist, graph, signalSpeed):
        count = 1 if dist % signalSpeed == 0 else 0
        for neighbor, weight in graph[node]:
            if neighbor != parent:
                count += self.dfs(neighbor, node, dist + weight, graph, signalSpeed)
        return count

    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        graph = defaultdict(list)
        for u, v, weight in edges:
            graph[u].append((v, weight))
            graph[v].append((u, weight))

        num_servers = len(edges) + 1
        result = []

        for node in range(num_servers):
            total_servers = 0
            connectable_pairs = 0
            for neighbor, weight in graph[node]:
                valid_nodes = self.dfs(neighbor, node, weight, graph, signalSpeed)
                connectable_pairs += total_servers * valid_nodes
                total_servers += valid_nodes
            
            result.append(connectable_pairs)

        return result