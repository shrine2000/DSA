import java.util.ArrayList;
import java.util.List;

public class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        if (triangle == null || triangle.size() == 0)
            return 0;

        int n = triangle.size();
        int[][] dp = new int[n][n];

        for (int i = 0; i < n; i++)
            dp[n - 1][i] = triangle.get(n - 1).get(i);

        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j <= i; j++) {
                dp[i][j] = triangle.get(i).get(j) + Math.min(dp[i + 1][j], dp[i + 1][j + 1]);
            }
        }

        return dp[0][0];
    }

    public static void main(String[] args) {
        // Sample usage
        List<List<Integer>> triangle = new ArrayList<>();
        triangle.add(List.of(2));
        triangle.add(List.of(3, 4));
        triangle.add(List.of(6, 5, 7));
        triangle.add(List.of(4, 1, 8, 3));

        Solution solution = new Solution();
        int result = solution.minimumTotal(triangle);
        System.out.println("Minimum total: " + result);
    }
}
