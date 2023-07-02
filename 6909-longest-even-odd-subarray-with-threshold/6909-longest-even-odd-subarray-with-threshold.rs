impl Solution {
    pub fn longest_alternating_subarray(nums: Vec<i32>, threshold: i32) -> i32 {
        let n = nums.len();
        let mut res = 0;
        
        for i in 0..n {
            for j in i..n {
                if nums[j] > threshold {
                    break;
                }
                
                if (j - i) % 2 == 1 && nums[j] % 2 == 0 {
                    break;
                }
                
                if (j - i) % 2 == 0 && nums[j] % 2 == 1 {
                    break;
                }
                
                res = res.max(j - i + 1);
            }
        }
        
        res as i32
    }
}