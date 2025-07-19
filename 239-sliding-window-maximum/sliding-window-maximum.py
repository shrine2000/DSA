class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        pq, res = [], []

        for i, val in enumerate(nums):
            heapq.heappush(pq, (-val, i))

            if i >= k - 1:
                while pq[0][1] <= i - k:
                    heapq.heappop(pq)
                res.append(-pq[0][0])

        return res


        
        
       