class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        counter = Counter(nums)
        for num, freq in counter.items():
            heapq.heappush(pq,(freq, num))
            if len(pq) > k:
                heapq.heappop(pq)
        return [num for _, num in pq]