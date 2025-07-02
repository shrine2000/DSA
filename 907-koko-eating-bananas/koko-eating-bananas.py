class Solution:
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            total_hours = sum(-(-pile // mid) for pile in piles)

            if total_hours <= h:
                right = mid
            else:
                left = mid + 1

        return left
