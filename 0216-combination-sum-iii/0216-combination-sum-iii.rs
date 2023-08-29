impl Solution {
    pub fn combination_sum3(k: i32, n: i32) -> Vec<Vec<i32>> {
        let nums: Vec<i32> = (1..=9).collect();
        let mut res: Vec<Vec<i32>> = Vec::new();

        fn bt(idx: usize, c: &mut Vec<i32>, nums: &Vec<i32>, res: &mut Vec<Vec<i32>>, k: i32, n: i32) {
            if c.len() == k as usize && c.iter().sum::<i32>() == n {
                res.push(c.clone());
                return;
            }

            if idx >= nums.len() {
                return;
            }

            c.push(nums[idx]);
            bt(idx + 1, c, nums, res, k, n);
            c.pop();
            bt(idx + 1, c, nums, res, k, n);
        }

        let mut c: Vec<i32> = Vec::new();
        bt(0, &mut c, &nums, &mut res, k, n);
        res
    }
}
