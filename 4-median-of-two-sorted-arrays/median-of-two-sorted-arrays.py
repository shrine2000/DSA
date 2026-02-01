class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pq = []

        for num in nums1:
            heapq.heappush(pq, (num))
        for num in nums2:
            heapq.heappush(pq, (num))

        n = len(pq)
        if n % 2 == 1:
            mid = n // 2
            for _ in range(mid):
                heapq.heappop(pq)
            return heapq.heappop(pq)
        else:
            mid = n // 2
            for _ in range(mid - 1):
                heapq.heappop(pq)
            a = heappop(pq)
            b = heappop(pq)
            return (a + b) / 2
