impl Solution {
    fn dfs(grid: &mut Vec<Vec<i32>>, i: usize, j: usize, dist: i32) {
        let rows = grid.len();
        let cols = grid[0].len() as i32;

        if i >= rows || j >= cols as usize || grid[i][j] != 0 && grid[i][j] <= dist {
            return;
        }

        grid[i][j] = dist;

        let directions: [(i32, i32); 4] = [(0, 1), (0, -1), (1, 0), (-1, 0)];
        for (dx, dy) in directions.iter() {
            let nx = (i as i32 + dx) as usize;
            let ny = (j as i32 + dy) as usize;
            Self::dfs(grid, nx, ny, dist + 1);
        }
    }

    pub fn max_distance(grid: Vec<Vec<i32>>) -> i32 {
        let mut grid = grid;
        let rows = grid.len();
        let cols = grid[0].len();

        let mut max_dist = -1;

        for i in 0..rows {
            for j in 0..cols {
                if grid[i][j] == 1 {
                    grid[i][j] = 0;
                    Self::dfs(&mut grid, i, j, 1);
                }
            }
        }

        for i in 0..rows {
            for j in 0..cols {
                if grid[i][j] > 1 {
                    max_dist = max_dist.max(grid[i][j] - 1);
                }
            }
        }

        max_dist
    }
}
