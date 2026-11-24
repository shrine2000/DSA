class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        N = len(coins)

        @cache
        def dfs(idx, remaining):
            if remaining == 0:
                return 1

            if idx < 0 or remaining < 0:
                return 0

            pick = dfs(idx - 1, remaining)
            not_pick = dfs(idx, remaining - coins[idx])

            return pick + not_pick

        return dfs(N - 1, amount)
