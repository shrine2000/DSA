impl Solution {
    pub fn find_kth_positive(arr: Vec<i32>, k: i32) -> i32 {
        let mut result = Vec::new();
        
        for i in 1..=arr.last().unwrap() + k {
            if !arr.contains(&i){
                result.push(i);
            }
        }
        
    
        result[k as usize -1]
    }
    
}