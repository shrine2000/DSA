impl Solution {
    pub fn number_of_employees_who_met_target(hours: Vec<i32>, target: i32) -> i32 {
        let mut count = 0;
        for &h in hours.iter() {
            if h >= target {
                count += 1;
            }
        }
        
        count
    }
}