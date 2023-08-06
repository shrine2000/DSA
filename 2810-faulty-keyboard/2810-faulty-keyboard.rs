impl Solution {
    pub fn final_string(s: String) -> String {
        let mut res = String::new();
        for c in s.chars() {
            if c == 'i' {
                let r: String = res.chars().rev().collect();
                res = r;
            } else {
                res.push(c);
            }
        }
        res
    }
}