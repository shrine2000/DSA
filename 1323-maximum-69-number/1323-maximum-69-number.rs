impl Solution {
    pub fn maximum69_number(num: i32) -> i32 {
        let mut target: Vec<i32> = num
            .to_string()
            .chars()
            .map(|c| c.to_digit(10).unwrap() as i32)
            .collect();

        let mut max_number: i32 = num;

        for i in 0..target.len() {
            if target[i] == 6 {
                target[i] = 9;
                let temp_max_number: i32 = target
                    .iter()
                    .fold(0, |acc, &digit| acc * 10 + digit);
                max_number = max_number.max(temp_max_number);
                target[i] = 6; 
            }
        }

        max_number
    }
}
