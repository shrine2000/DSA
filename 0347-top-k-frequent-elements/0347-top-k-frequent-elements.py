from typing import List
from itertools import islice


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)

        pq = []

        for v, f in freq_map.items():
            heapq.heappush(pq, (f, v))
            if len(pq) > k:
                heapq.heappop(pq)

        ans = [item[1] for item in pq]

        return ans
