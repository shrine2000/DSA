impl Solution {
    pub fn count_symmetric_integers(low: i32, high: i32) -> i32 {
        fn is_symmetric(n: i32) -> bool {
            let s = n.to_string();
            let len = s.len();
            if len % 2 != 0 {
                return false; 
            }
            
            let half_len = len / 2;
            let left_sum: i32 = s.chars().take(half_len).map(|c| c.to_digit(10).unwrap() as i32).sum();
            let right_sum: i32 = s.chars().skip(half_len).map(|c| c.to_digit(10).unwrap() as i32).sum();
            
            left_sum == right_sum
        }
        
        let mut count = 0;
        for num in low..=high {
            if is_symmetric(num) {
                count += 1;
            }
        }
        
        count
    }
}
