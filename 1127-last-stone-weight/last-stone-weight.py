class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-stone for stone in stones]
        heapq.heapify(pq)
        while pq and len(pq) > 1:
            x = heapq.heappop(pq)
            y = heapq.heappop(pq)
            if x != y:
                heapq.heappush(pq, -(y - x))
        return -pq[0] if pq else 0
