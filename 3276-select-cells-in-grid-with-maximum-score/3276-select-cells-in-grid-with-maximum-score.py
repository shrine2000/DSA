class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        unique_values = sorted(set(val for row in grid for val in row), reverse=True)
        
        value_positions = {val: [] for val in unique_values}
        for i in range(m):
            for j in range(n):
                value_positions[grid[i][j]].append(i)
        
        dp = [0] * (1 << m)
        
        for value in unique_values:
            temp_dp = dp.copy()
            
            for row in value_positions[value]:
                for mask in range(1 << m):
                    if mask & (1 << row) == 0:
                        new_mask = mask | (1 << row)
                        temp_dp[new_mask] = max(temp_dp[new_mask], dp[mask] + value)
            
            dp = temp_dp
        
        return max(dp)
