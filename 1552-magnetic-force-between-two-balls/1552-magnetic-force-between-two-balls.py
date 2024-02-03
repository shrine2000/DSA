from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        left = 0
        right = position[-1] - position[0]
        result = 0

        while left <= right:
            mid = (left + right) // 2

            if self.isPossible(position, m, mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result

    def isPossible(self, position: List[int], m: int, force: int) -> bool:
        count = 1
        prev_pos = position[0]

        for i in range(1, len(position)):
            if position[i] - prev_pos >= force:
                count += 1
                prev_pos = position[i]

            if count >= m:
                return True

        return False
