class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        ballons = [1] + nums + [1]
        n = len(ballons)

        @cache
        def dp(l, r):
            if r - l <= 1:
                return 0

            best = 0
            for k in range(l + 1, r):
                coins = dp(l, k) + ballons[l] * ballons[k] * ballons[r] + dp(k, r)
                best = max(best, coins)
            return best

        return dp(0, n - 1)
