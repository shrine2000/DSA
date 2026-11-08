class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        N = len(flowerbed)
        count = n
        for i in range(N):
            if (
                flowerbed[i] == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == N - 1 or flowerbed[i + 1] == 0)
            ):
                flowerbed[i] = 1
                count -= 1
                if count == 0:
                    return True
        return count == 0
