from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        
        heap = [(-freq, num) for num, freq in freq_map.items()]
        heapq.heapify(heap)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
