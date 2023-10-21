impl Solution {
    pub fn minimum_mountain_removals(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        
        let mut lis_left = vec![1; n];
        let mut lis_right = vec![1; n];
        
        // Compute the LIS from the left.
        for i in 0..n {
            for j in 0..i {
                if nums[i] > nums[j] {
                    lis_left[i] = lis_left[i].max(1 + lis_left[j]);
                }
            }
        }
        
        // Compute the LIS from the right.
        for i in (0..n).rev() {
            for j in (i..n).rev() {
                if nums[i] > nums[j] {
                    lis_right[i] = lis_right[i].max(1 + lis_right[j]);
                }
            }
        }
        
        let mut max_mountain = 0;
        
        // Find the maximum mountain length by combining the LIS from both ends.
        for i in 0..n {
            if lis_left[i] > 1 && lis_right[i] > 1 {
                max_mountain = max_mountain.max(lis_left[i] + lis_right[i] - 1);
            }
        }
        
        // Calculate the minimum number of elements to remove.
        if max_mountain > 0 {
            n as i32 - max_mountain as i32
        } else {
            -1
        }
    }
}
