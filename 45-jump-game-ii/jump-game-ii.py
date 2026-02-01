from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(idx: int) -> int:
            # If we've reached or passed the last index, no more jumps needed
            if idx >= n - 1:
                return 0

            # If current position is zero, we cannot jump forward
            if nums[idx] == 0:
                return float("inf")  # Use infinity to represent unreachable state

            min_jumps = float("inf")  # Track minimum jumps from this index

            # Try all jump lengths from 1 to nums[idx]
            for step in range(1, nums[idx] + 1):
                new_pos = idx + step
                if new_pos < n:
                    jumps = dfs(new_pos)
                    if jumps != float("inf"):
                        min_jumps = min(min_jumps, jumps + 1)  # +1 for current jump

            return min_jumps

        result = dfs(0)
        return result if result != float("inf") else -1  # Return -1 if unreachable
