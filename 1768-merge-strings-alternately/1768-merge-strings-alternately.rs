impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let mut ans = String::new();
        let (mut i, mut j) = (0, 0);

        while i < word1.len() && j < word2.len() {
            ans.push(word1.chars().nth(i).unwrap());
            ans.push(word2.chars().nth(j).unwrap());
            i += 1;
            j += 1;
        }

        if i != word1.len() {
            ans.push_str(&word1[i..]);
        }

        if j != word2.len() {
            ans.push_str(&word2[j..]);
        }

        ans
    }
}
