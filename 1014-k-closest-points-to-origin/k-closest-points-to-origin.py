class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []

        for x, y in points:
            dist = x * x + y * y

            heapq.heappush(pq, (-dist, [x, y]))
            if len(pq) > k:
                heapq.heappop(pq)
        return [point for _, point in pq]
