class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def helper(current, amount):
            if current >= len(coins) or amount <= 0:
                return 0 if amount == 0 else float('inf')
            notTake = 0  + helper(current + 1, amount)   
            take = float('inf')
            if coins[current] <= amount:
                take = 1 + helper(current, amount - coins[current])
            res = min(notTake, take)
            return res
        result = helper(0, amount)
        return result if result != float('inf') else -1
        
        

        