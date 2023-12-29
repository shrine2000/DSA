impl Solution {
    pub fn incremovable_subarray_count(nums: Vec<i32>) -> i32 {
        let mut count = 0;
        let length = nums.len();

        for i in 0..length {
            for j in i..length {
                let sub_arr = &nums[i..=j];
                let mut temp = nums.clone();
                temp.splice(i..=j, [].iter().cloned());

                let strictly_increasing = temp.windows(2).all(|w| w[0] < w[1]);

                if strictly_increasing {
                    count += 1;
                }
            }
        }

        count
    }
}
