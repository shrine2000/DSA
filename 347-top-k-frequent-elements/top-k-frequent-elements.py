class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        counter = Counter(nums)

        pq = []

        for key, value in counter.items():
            heapq.heappush(pq, (value, key))
            if len(pq) > k:
                heapq.heappop(pq)
        return [key for _, key in pq]