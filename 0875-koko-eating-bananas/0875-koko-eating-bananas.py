from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = max(piles)

        while min_speed < max_speed:
            mid_speed = (min_speed + max_speed) // 2
            total_hours = sum(math.ceil(pile / mid_speed) for pile in piles)
            if total_hours > h:
                min_speed = mid_speed + 1
            else:
                max_speed = mid_speed

        return min_speed


def test_minEatingSpeed():
    solution = Solution()

    # Test case 1
    piles1 = [3, 6, 7, 11]
    h1 = 8
    assert solution.minEatingSpeed(piles1, h1) == 4

    # Test case 2
    piles2 = [30, 11, 23, 4, 20]
    h2 = 5
    assert solution.minEatingSpeed(piles2, h2) == 30

    # Test case 3
    piles3 = [30, 11, 23, 4, 20]
    h3 = 6
    assert solution.minEatingSpeed(piles3, h3) == 23

    print("All test cases pass")


test_minEatingSpeed()
