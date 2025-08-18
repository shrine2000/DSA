class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(k):
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
            return total <= h

        left, right = 1, max(piles)
        res = right
        while left <= right:
            mid = (left + right) // 2
            if canEat(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
