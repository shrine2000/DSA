class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        count = Counter(nums)


        for key, value in count.items():
            heapq.heappush(pq, (value, key))

            if len(pq) > k:
                heapq.heappop(pq)
        return [key for _, key in pq]