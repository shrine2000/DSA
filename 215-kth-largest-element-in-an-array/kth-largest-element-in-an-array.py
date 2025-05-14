class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = [-num for num in nums]
        heapq.heapify(pq)
        for _ in range(k - 1):
            heapq.heappop(pq)
        return -pq[0]


# 6 5 4 3 2 1
