class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(idx, remaining):
            if (idx, remaining) in memo:
                return memo[(idx, remaining)]

            if remaining == 0:
                return 0
            if idx == len(coins) or remaining < 0:
                return float("inf")

            pick = 1 + dfs(idx, remaining - coins[idx])
            not_pick = dfs(idx + 1, remaining)

            res =  min(pick, not_pick)
            memo[(idx, remaining)] = res
            return res
        count = -1 if dfs(0, amount) == float('inf') else dfs(0, amount) 
        return count
