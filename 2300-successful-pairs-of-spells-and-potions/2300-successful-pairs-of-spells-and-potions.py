class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()

        n = len(spells)
        m = len(potions)

        pairs = [0] * n

        for i in range(n):
            left = 0
            right = m - 1
            temp = 0

            while left <= right:
                mid = left + (right - left) // 2
                if spells[i] * potions[mid] >= success:
                    temp = m - mid
                    right = mid - 1
                else:
                    left = mid + 1

            pairs[i] = temp

        return pairs
