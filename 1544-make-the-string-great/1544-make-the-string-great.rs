impl Solution {
    pub fn make_good(s: String) -> String {
        let mut stack: Vec<char> = Vec::new();
        
        for c in s.chars() {
            if let Some(top) = stack.last() {
                if top.is_uppercase() && top.to_ascii_lowercase() == c {
                    stack.pop();
                } else if top.is_lowercase() && top.to_ascii_uppercase() == c {
                    stack.pop();
                } else {
                    stack.push(c);
                }
            } else {
                stack.push(c);
            }
        }
        
        stack.iter().collect()
    }
}
