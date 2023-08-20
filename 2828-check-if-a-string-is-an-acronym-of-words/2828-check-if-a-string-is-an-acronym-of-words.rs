impl Solution {
    pub fn is_acronym(words: Vec<String>, s: String) -> bool {
        let formed_acronym: String = words.iter().map(|w| w.chars().next().unwrap()).collect();
        formed_acronym == s
    }
}
