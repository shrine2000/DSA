class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        def can_bloom(day):
            bouquets = 0
            flowers = 0

            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            return bouquets >= m

        left, right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = left + (right - left) // 2

            if can_bloom(mid):
                right = mid
            else:
                left = mid + 1

        return left
