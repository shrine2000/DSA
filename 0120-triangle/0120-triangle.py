
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        
        n = len(triangle)
        dp = [[0] * (i + 1) for i in range(n)]  
        
        dp[-1] = triangle[-1]
        
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
                
        return dp[0][0]