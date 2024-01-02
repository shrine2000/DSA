class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        pq = []
        for num in hand:
            heapq.heappush(pq, num)
        while pq:
            smallest = pq[0]
            for i in range(W):
                if smallest + i not in pq:
                    return False
                else:
                    pq.remove(smallest + i)
            heapq.heapify(pq)
        return True
