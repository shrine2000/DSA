class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = 1
        right = 10**14

        while left < right:
            mid = left + (right - left) // 2
            if self.isPossible(mid, time, totalTrips):
                right = mid
            else:
                left = mid + 1

        return left

    def isPossible(self, mid: int, time: List[int], totalTrips: int) -> bool:
        total = 0
        for t in time:
            total += mid // t

        return total >= totalTrips
