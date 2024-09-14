class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        max_heap = []
        result = []
        for i, (x, y) in enumerate(queries):
            dist = abs(x) + abs(y)
            heapq.heappush(max_heap, -dist)
            if len(max_heap) > k:
                heapq.heappop(max_heap)
            if len(max_heap) < k:
                result.append(-1)
            else:
                result.append(-max_heap[0])
        return result
