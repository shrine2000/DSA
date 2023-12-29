impl Solution {
    pub fn find_shortest_cycle(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let mut adj: Vec<Vec<i32>> = vec![vec![]; n as usize];
        for edge in edges.iter() {
            let u = edge[0] as usize;
            let v = edge[1] as usize;
            adj[u].push(v as i32);
            adj[v].push(u as i32);
        }
        
        let mut min_cycle = i32::MAX;
        for i in 0..n {
            let mut dist = vec![-1; n as usize];
            let mut queue = std::collections::VecDeque::new();
            queue.push_back(i);
            dist[i as usize] = 0;
            while let Some(u) = queue.pop_front() {
                for &v in adj[u as usize].iter() {
                    if dist[v as usize] == -1 {
                        dist[v as usize] = dist[u as usize] + 1;
                        queue.push_back(v);
                    } else if v != i && dist[v as usize] >= dist[u as usize] {
                        min_cycle = min_cycle.min(dist[u as usize] + dist[v as usize] + 1);
                    }
                }
            }
        }
        
        if min_cycle == i32::MAX {
            -1
        } else {
            min_cycle
        }
    }
}
