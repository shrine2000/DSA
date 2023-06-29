impl Solution {
    pub fn max_distance(position: Vec<i32>, m: i32) -> i32 {
        let mut position = position;
        position.sort();
        
        let mut left = 0;
        let mut right = position[position.len() -1] - position[0];
        let mut result = 0;
        while left <= right {
            let mid = (left + right) / 2;
            
            if Self::is_possible(&position, m ,mid){
                result = mid;
                left = mid + 1;
            } else {
                right = mid - 1
            }
        }
        
        result
    }
    
    fn is_possible(position: &Vec<i32>, m: i32, force: i32) -> bool {
        let mut count = 1;
        let mut prev_pos = position[0];
        for i in 1..position.len(){
            if position[i] - prev_pos >= force {
                count += 1;
                prev_pos = position[i];
            }
            
            if count >=m {
                return true;
            }
            
        }
        
        false
    }
}