impl Solution {
    pub fn largest_sum_of_averages(nums: Vec<i32>, k: i32) -> f64 {
        let n = nums.len();
        let mut m = vec![vec![0.0; n + 1]; k as usize + 1];

        fn helper(nums: &Vec<i32>, k: i32, p: usize, m: &mut Vec<Vec<f64>>) -> f64 {
            let n = nums.len();
            if p >= n || m[k as usize][p] > 0.0 {
                return m[k as usize][p];
            }

            let mut s = 0.0;
            for i in p..(n - k as usize + 1) {
                s += nums[i] as f64;
                if k == 1 && i < n - 1 {
                    continue;
                }
                m[k as usize][p] = m[k as usize][p].max(s / (i - p + 1) as f64 + helper(nums, k - 1, i + 1, m));
            }

            m[k as usize][p]
        }

        helper(&nums, k, 0, &mut m) as f64
    }
}
