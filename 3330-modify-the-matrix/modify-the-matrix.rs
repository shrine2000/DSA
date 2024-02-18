impl Solution {
    pub fn modified_matrix(matrix: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        if matrix.is_empty() || matrix[0].is_empty() {
            return vec![];
        }

        let rows = matrix.len();
        let cols = matrix[0].len();
        let mut answer = matrix.clone();

        for j in 0..cols {
            let mut max_value = i32::MIN;
            for i in 0..rows {
                if matrix[i][j] == -1 {
                    continue;
                }
                max_value = max_value.max(matrix[i][j]);
            }

            for i in 0..rows {
                if matrix[i][j] == -1 {
                    answer[i][j] = max_value;
                }
            }
        }

        answer
    }
}
 