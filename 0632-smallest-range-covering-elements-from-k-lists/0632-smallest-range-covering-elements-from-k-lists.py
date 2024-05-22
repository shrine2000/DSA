import heapq
from typing import List, Tuple


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> Tuple[int, int]:
        min_heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(min_heap)

        smallest_range = -float("inf"), float("inf")
        max_end = max(row[0] for row in nums)

        while min_heap:
            start_val, row_idx, col_idx = heapq.heappop(min_heap)

            if max_end - start_val < smallest_range[1] - smallest_range[0]:
                smallest_range = start_val, max_end

            if col_idx + 1 == len(nums[row_idx]):
                return smallest_range

            next_val = nums[row_idx][col_idx + 1]

            max_end = max(max_end, next_val)

            heapq.heappush(min_heap, (next_val, row_idx, col_idx + 1))

        return smallest_range
