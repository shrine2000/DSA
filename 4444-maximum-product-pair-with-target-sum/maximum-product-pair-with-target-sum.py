class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        def is_valid(i, j):
            return bool(nums[i] > nums[j] and nums[i] + nums[j] == target)

        pq = []
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if is_valid(i, j):
                    product = nums[i] * nums[j]
                    heapq.heappush(pq, (-product, i, j))
        if pq:
            _, x, y = heapq.heappop(pq)
            return [x, y]
        return [-1, -1]
