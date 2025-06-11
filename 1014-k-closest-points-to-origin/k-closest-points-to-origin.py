class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def _get_dist(x, y):
            return sqrt(x**2 + y**2)

        pq = []
        for point in points:
            dist = _get_dist(point[0], point[1])
            heapq.heappush(pq, (-dist, point))
            if len(pq) > k:
                heapq.heappop(pq)
        return [point for _, point in pq]
