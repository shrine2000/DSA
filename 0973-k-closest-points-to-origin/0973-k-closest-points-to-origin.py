class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return math.sqrt(point[0] ** 2 + point[1] ** 2)
        
        pq = []
        
        for point in points:
            dist = distance(point)
            heapq.heappush(pq, (-dist, point))
            if len(pq) > k:
                heapq.heappop(pq)
                
        result = [point for _, point in pq]
        return result
        
        