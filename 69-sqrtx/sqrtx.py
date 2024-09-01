class Solution:
    def mySqrt(self, x: int) -> int:
        def check(y):
            return y * y

        left, right = 0, x + 1

        while left < right:
            mid = left + (right - left) // 2
            if check(mid) > x:
                right = mid
            else:
                left = mid + 1

        return left - 1
