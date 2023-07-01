### Brute Force
Will get TLE
```
impl Solution {
    pub fn minimum_time(time: Vec < i32 > , total_trips: i32) -> i64 {
        let mut trips: i32 = 0;
        let mut t: i32 = 1;
        while trips < total_trips {
                for i in 0..time.len() {
                    if t % time[i] == 0 {
                        trips += 1;
                    }
                }
                t += 1;
            }
            (t - 1) as i64
    }
}
```
​
​
