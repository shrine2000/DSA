class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        heap = []
        ans = max(nums)

        for i in range(len(nums)):
            while heap and i - heap[0][1] > k:
                heappop(heap)

            best = max(0, -heap[0][0] if heap else 0)
            curr = best + nums[i]
            ans = max(ans, curr)
            heappush(heap, (-curr, i))

        return ans
