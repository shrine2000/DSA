class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for point in points:
            x, y = point[0], point[1]
            dist = sqrt(x**2 + y**2)
            heapq.heappush(pq, (-dist, point))
            if len(pq) > k:
                heapq.heappop(pq)
        return [point for _, point in pq]
