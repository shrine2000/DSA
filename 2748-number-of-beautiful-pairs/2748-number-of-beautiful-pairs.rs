impl Solution {
    pub fn count_beautiful_pairs(nums: Vec<i32>) -> i32 {
        let mut count = 0;

        for i in 0..nums.len() {
            for j in (i + 1)..nums.len() {
                let s = nums[i].to_string();
                let st = nums[j].to_string();
                if Self::gcd(s.chars().next().unwrap() as i32 - '0' as i32, st.chars().last().unwrap() as i32 - '0' as i32) == 1 {
                    count += 1;
                }
            }
        }

        count
    }

    fn gcd(x: i32, y: i32) -> i32 {
        if y == 0 {
            x
        } else {
            Self::gcd(y, x % y)
        }
    }
}
