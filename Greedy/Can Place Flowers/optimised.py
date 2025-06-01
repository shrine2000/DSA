from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Pad the flowerbed with virtual zeros on both sides
        padded_flowerbed = [0] + flowerbed + [0]
        total_plots = len(padded_flowerbed)

        # Iterate from the second element to the second-last
        for i in range(1, total_plots - 1):
            # If the previous, current, and next plots are empty, plant a flower
            if (
                padded_flowerbed[i - 1] == 0
                and padded_flowerbed[i] == 0
                and padded_flowerbed[i + 1] == 0
            ):
                padded_flowerbed[i] = 1  # Plant the flower
                n -= 1  # Decrement flowers to plant
                if n == 0:  # Early return if goal met
                    return True

        # If all flowers planted, return True
        return n <= 0
