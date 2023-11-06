impl Solution {
    pub fn number_of_paths(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut dp = vec![vec![vec![0; k as usize]; n]; m];
        let mod_val = 1_000_000_007;

        dp[0][0][grid[0][0] as usize % k as usize] = 1;

        for x in 0..m {
            for y in 0..n {
                for z in 0..k as usize {
                    if x > 0 {
                        dp[x][y][(z + grid[x][y] as usize) % k as usize] += dp[x - 1][y][z];
                        dp[x][y][(z + grid[x][y] as usize) % k as usize] %= mod_val;
                    }
                    if y > 0 {
                        dp[x][y][(z + grid[x][y] as usize) % k as usize] += dp[x][y - 1][z];
                        dp[x][y][(z + grid[x][y] as usize) % k as usize] %= mod_val;
                    }
                }
            }
        }

        dp[m - 1][n - 1][0]
    }
}
