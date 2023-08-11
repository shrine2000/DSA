import heapq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, -num)   
        
        max1 = -heapq.heappop(heap)
        max2 = -heapq.heappop(heap)
        
        return (max1 - 1) * (max2 - 1)
