class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        heap = []
        for i in range(0, len(nums), 2):
            arr = str(nums[i]) + str(nums[i + 1])
            heapq.heappush(heap, int(arr))
        return heap[0]