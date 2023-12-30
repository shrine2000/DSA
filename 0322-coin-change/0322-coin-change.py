from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 
        
        coins.sort()
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin > i:
                    break
                
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
