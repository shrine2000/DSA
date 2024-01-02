import heapq


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        pq = []
        res = 0

        for num in nums:
            heapq.heappush(pq, -num)

        while pq and k > 0:
            top_element = -heapq.heappop(pq)
            res += top_element

            next_element = top_element + 1
            heapq.heappush(pq, -next_element)

            k -= 1

        return res
