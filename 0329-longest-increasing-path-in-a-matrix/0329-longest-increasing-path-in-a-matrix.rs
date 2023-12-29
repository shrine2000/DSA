impl Solution {
    pub fn longest_increasing_path(matrix: Vec<Vec<i32>>) -> i32 {
        let m = matrix.len();
        let n = matrix[0].len();
        
        fn dfs(matrix: &Vec<Vec<i32>>, i: usize, j: usize, prev: i32, memo: &mut Vec<Vec<i32>>) -> i32 {
            if i >= matrix.len() || j >= matrix[0].len() || matrix[i][j] <= prev {
                return 0;
            }
            
            if memo[i][j] != 0 {
                return memo[i][j];
            }
            
            let left = dfs(matrix, i, j.wrapping_sub(1), matrix[i][j], memo);
            let right = dfs(matrix, i, j + 1, matrix[i][j], memo);
            let top = dfs(matrix, i.wrapping_sub(1), j, matrix[i][j], memo);
            let bottom = dfs(matrix, i + 1, j, matrix[i][j], memo);
            
            let max_lr = left.max(right);
            let max_tb = top.max(bottom);
            let result = 1 + max_lr.max(max_tb);
            memo[i][j] = result;
            result
        }
        
        let mut memo = vec![vec![0; n]; m];
        let mut ans = 1;
        
        for i in 0..m {
            for j in 0..n {
                let path = dfs(&matrix, i, j, std::i32::MIN, &mut memo);
                ans = ans.max(path);
            }
        }
        
        ans
    }
}
