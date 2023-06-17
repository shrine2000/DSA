use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut groups: HashMap<Vec<char>, Vec<String>> = HashMap::new();
        
        for word in strs {
            let mut chars: Vec<char> = word.chars().collect();
            chars.sort();
            groups.entry(chars).or_insert(Vec::new()).push(word);
        }
        
        groups.values().cloned().collect()
    }
}