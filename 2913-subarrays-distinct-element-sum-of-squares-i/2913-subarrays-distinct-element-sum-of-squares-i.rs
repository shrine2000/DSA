impl Solution {
    pub fn sum_counts(nums: Vec<i32>) -> i32 {
        let mut total = 0;
        let n = nums.len();
        
        for i in 0..n {
            for j in i..n {
                let sa = &nums[i..=j];
                let dc = sa.iter().collect::<std::collections::HashSet<_>>().len();
                total += (dc * dc) as i32;
            }
        }
        
        total
    }
}