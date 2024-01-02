class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def isPossible(mid, price, k):
            prev = price[0]
            count = 0

            for i in range(1, len(price)):
                if price[i] - prev >= mid:
                    prev = price[i]
                    count += 1

            count += 1
            return count >= k

        price.sort()

        left, right = 0, price[-1] - price[0]
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2
            if isPossible(mid, price, k):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
