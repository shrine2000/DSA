from typing import List
from itertools import islice

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        
        for num in nums:
            if num in hmap:
                hmap[num] += 1
            else:
                hmap[num] = 1
        
        sorted_hmap = dict(sorted(hmap.items(), key=lambda x: x[1], reverse=True))
        
        return list(islice(sorted_hmap.keys(), k))
