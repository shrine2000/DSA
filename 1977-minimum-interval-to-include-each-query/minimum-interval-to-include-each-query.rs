use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn min_interval(intervals: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
        let mut intervals = intervals;
        let mut queries_with_idx: Vec<(i32, usize)> = queries.iter().enumerate()
            .map(|(i, &q)| (q, i)).collect();
        intervals.sort_unstable_by_key(|i| i[0]);
        queries_with_idx.sort_unstable();

        let mut res = vec![-1; queries.len()];
        let mut heap = BinaryHeap::new();
        let mut i = 0;

        for (q, idx) in queries_with_idx {
            while i < intervals.len() && intervals[i][0] <= q {
                let (start, end) = (intervals[i][0], intervals[i][1]);
                if end >= q {
                    heap.push(Reverse((end - start + 1, end)));
                }
                i += 1;
            }
            while let Some(&Reverse((_, end))) = heap.peek() {
                if end < q {
                    heap.pop();
                } else {
                    break;
                }
            }
            if let Some(&Reverse((len, _))) = heap.peek() {
                res[idx] = len;
            }
        }

        res
    }
}
