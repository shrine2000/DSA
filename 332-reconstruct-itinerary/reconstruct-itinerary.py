class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        result = []

        def dfs(node):
            while graph[node]:
                dfs(heapq.heappop(graph[node]))
            result.append(node)

        dfs("JFK")
        return result[::-1]
