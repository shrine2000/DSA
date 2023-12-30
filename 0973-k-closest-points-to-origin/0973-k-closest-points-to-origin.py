class Solution:
    
    """
    heapq.heappushpop() is a function provided by the heapq module in Python that combines two operations: pushing a new element onto a heap and then popping the smallest element from the heap. It is often used to maintain a fixed-size heap where you want to replace the smallest element with a new element if the new element is larger than the smallest element.
    
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        
        for (x, y) in points:
            dist = - (x * x + y * y)
            if len(pq) == k:
                heapq.heappushpop(pq, (dist, x, y))
            else:
                heapq.heappush(pq, (dist, x, y))
                
        return [(x, y) for (dist, x, y) in pq]
        