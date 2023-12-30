class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []
        
        for num in nums:
            heapq.heappush(heap, -num)
        
        i = -heapq.heappop(heap)
        j = -heapq.heappop(heap)
        
        return (i -1) * (j- 1)