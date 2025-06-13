from collections import defaultdict
import heapq
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        pq = []
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1
        
        for word, count in freq.items():
            heapq.heappush(pq, (-count, word))  
          
        print(pq)
        
        return [heapq.heappop(pq)[1] for _ in range(k)]
