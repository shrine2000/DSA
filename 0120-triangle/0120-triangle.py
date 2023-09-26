from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        
        dp = [0] * len(triangle)
        dp[0] = triangle[0][0]
        
        for i in range(1, len(triangle)):
            dp[i] = dp[i - 1] + triangle[i][-1]
            
            for j in range(len(triangle[i]) - 2, 0, -1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j - 1])
                
            dp[0] += triangle[i][0]
        
        min_path_sum = min(dp)
        
        return min_path_sum
