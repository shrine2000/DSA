class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def recursive(idx, remaining):
            if remaining == 0:
                return 1
            if idx >= len(coins) or remaining < 0:
                return 0
            pick = recursive(idx, remaining - coins[idx])
            not_pick = recursive(idx + 1, remaining)
            return pick + not_pick
        count = recursive(0, amount)
        return count
