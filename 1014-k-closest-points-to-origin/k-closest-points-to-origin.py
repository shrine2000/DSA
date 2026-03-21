class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []

        for point in points:
            x, y = point[0], point[1]
            heapq.heappush(pq, (-(x * x + y * y), point[0], point[1]))
            if len(pq) > k:
                heapq.heappop(pq)
        return [[x, y] for (_, x, y) in pq]
