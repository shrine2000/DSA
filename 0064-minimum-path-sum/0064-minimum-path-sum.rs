impl Solution {
    pub fn min_path_sum(grid: Vec<Vec<i32>>) -> i32 {
        if grid.is_empty() || grid[0].is_empty() {
            return 0;
        }
        
        let n = grid.len();
        let m = grid[0].len();
        
        let mut dp = vec![vec![0; m]; n];
        
        dp[0][0] = grid[0][0];
        
        for i in 1..m {
            dp[0][i] = dp[0][i - 1] + grid[0][i];
        }
        
        for j in 1..n {
            dp[j][0] = dp[j - 1][0] + grid[j][0];
        }
        
        for i in 1..n {
            for j in 1..m {
                dp[i][j] = std::cmp::min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
            }
        }
        
        dp[n - 1][m - 1]
    }
}
