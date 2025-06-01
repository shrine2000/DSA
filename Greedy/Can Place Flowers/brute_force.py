from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        total_plots = len(flowerbed)

        for i in range(total_plots):
            # Check if the current plot is empty
            if flowerbed[i] == 0:
                # Check if left and right plots are empty or out of bounds
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == total_plots - 1) or (flowerbed[i + 1] == 0)

                # If both sides are empty, we can plant a flower here
                if empty_left and empty_right:
                    flowerbed[i] = 1  # Plant flower
                    n -= 1  # Decrement the flower count
                    if n == 0:  # Early exit if all flowers are planted
                        return True

        # If we finish the loop and have placed enough flowers, return True
        return n <= 0
