class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        pq = []

        for value, occurrences in count.items():
            heapq.heappush(pq, (occurrences, value))
            if len(pq) > k:
                heapq.heappop(pq)

        return [val for _, val in pq]
