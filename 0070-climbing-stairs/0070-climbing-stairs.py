class Solution:
    def climbStairs(self, n: int) -> int:
        def findWays(dp, n):
            if n <= 1:
                return 1
            
            if dp[n] != -1:
                return dp[n]
            dp[n] = findWays(dp, n - 1) + findWays(dp, n - 2)
            return dp[n]
        
        dp = [-1] * (n + 1)
        return findWays(dp, n)
       