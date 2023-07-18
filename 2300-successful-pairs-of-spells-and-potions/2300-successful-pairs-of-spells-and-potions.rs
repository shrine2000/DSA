impl Solution {
    pub fn successful_pairs(spells: Vec<i32>, potions: Vec<i32>, success: i64) -> Vec<i32> {
        let mut indices: Vec<usize> = (0..spells.len()).collect();
        indices.sort_by_key(|&i| spells[i]);
        
        let mut sorted_potions = potions.clone();
        sorted_potions.sort_unstable_by(|a, b| b.cmp(a));
        
        let mut result: Vec<i32> = vec![0; spells.len()];
        
        let mut j = 0;
        for &i in &indices {
            while j < sorted_potions.len() && sorted_potions[j] as i64 * spells[i] as i64 >= success {
                j += 1;
            }
            
            result[i] = j as i32;
        }
    
        result
    }
}
