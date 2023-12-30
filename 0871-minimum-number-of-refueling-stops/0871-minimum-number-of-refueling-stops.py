import heapq
from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        pq = []
        stations.append((target, float('inf')))
        ans = prev = 0
        for p, f in stations:
            startFuel -= p - prev
            while pq and startFuel < 0:
                startFuel += -heapq.heappop(pq)
                ans += 1
            if startFuel < 0:
                return -1
            heapq.heappush(pq, -f)
            prev = p
            
        return ans
