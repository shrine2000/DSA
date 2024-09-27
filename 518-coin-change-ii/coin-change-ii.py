class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def helper(idx, remaining_amount):
            if remaining_amount == 0:
                return 1
            if remaining_amount < 0:
                return 0

            if idx == len(coins):
                return 0

            take = helper(idx, remaining_amount - coins[idx]) 
            not_take = helper(idx + 1, remaining_amount) 

            return take + not_take

        return helper(0, amount)