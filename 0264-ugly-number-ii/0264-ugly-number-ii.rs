use std::collections::{BinaryHeap, HashSet};
use std::cmp::Reverse;

impl Solution {
    pub fn nth_ugly_number(n: i32) -> i32 {
        let mut heap = BinaryHeap::new();
        let mut seen = HashSet::new();
        let mut nums = Vec::new();
        
        heap.push(Reverse(1i64));
        seen.insert(1i64);
        
        while nums.len() < n as usize {
            let su = heap.pop().unwrap().0;
            nums.push(su);
            
            for &f in &[2, 3, 5] {
                let nu = f * su;
                if !seen.contains(&nu){
                    heap.push(Reverse(nu));
                    seen.insert(nu);
                }
            }
        }
        
        nums[n as usize - 1] as i32
    }
}
