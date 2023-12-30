import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            heapq.heappush(pq, -num)
        
        while pq and k > 0:
            if k == 1:
                return -heapq.heappop(pq)
            else: 
                heapq.heappop(pq)
            k -= 1   
