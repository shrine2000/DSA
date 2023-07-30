use std::collections::BinaryHeap;

impl Solution {
    pub fn maximize_sum(nums: Vec<i32>, k: i32) -> i32 {
        let mut pq = BinaryHeap::new();
        let mut res = 0;
        for num in nums {
            pq.push(num);
        }
        
        for _ in 0..k {
            let top_elem = pq.pop().unwrap();
            res += top_elem;
            
            let next_elem = top_elem + 1;
            pq.push(next_elem)
        }
        
        
        res
    }
}