class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq = []
        count = 0
        
        for row in matrix:
            for num in row:
                heapq.heappush(pq, num)
                
        element = -1
        
        for _ in range(k):
            element = heapq.heappop(pq)
        
        return element
            