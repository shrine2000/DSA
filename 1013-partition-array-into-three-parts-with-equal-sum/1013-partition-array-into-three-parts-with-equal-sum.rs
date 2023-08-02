impl Solution {
    pub fn can_three_parts_equal_sum(arr: Vec<i32>) -> bool {
        let total_sum: i32 = arr.iter().sum();
        if total_sum % 3 != 0 {
            return false;
        }

        let target_sum = total_sum / 3;
        let mut sum1 = 0;
        let mut sum2 = 0;

        for i in 0..arr.len() - 1 {
            sum1 += arr[i];
            if sum1 == target_sum {
                for j in i + 1..arr.len() {
                    sum2 += arr[j];
                    if sum2 == target_sum && j < arr.len() - 1 {
                        return true;
                    }
                }
            }
        }

        false
    }
}
