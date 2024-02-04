impl Solution {
    pub fn minimum_time_to_initial_state(word: String, k: i32) -> i32 {
        fn z_function(s: &str) -> Vec<usize> {
            let n = s.len();
            let mut z = vec![0; n];
            z[0] = n;
            let (mut l, mut r) = (0, 0);

            for i in 1..n {
                if i <= r {
                    z[i] = std::cmp::min(z[i - l], r - i + 1);
                }
                while i + z[i] < n && s.chars().nth(z[i]).unwrap() == s.chars().nth(i + z[i]).unwrap() {
                    z[i] += 1;
                }
                if z[i] > r - i + 1 {
                    l = i;
                    r = i + z[i] - 1;
                }
            }

            z
        }

        let n = word.len();
        let z_values = z_function(&word);

        for i in (k as usize..n).step_by(k as usize) {
            if z_values[i] == n - i {
                return (i / k as usize) as i32;
            }
        }

        ((n + k as usize - 1) / k as usize) as i32
    }
}
