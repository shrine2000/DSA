class Solution {
    public int diagonalSum(int[][] mat) {
        int sum = 0;
        int n = mat.length;
        for (int i = 0; i < n; i++) {
            sum += mat[i][i]; // add elements from primary diagonal
            sum += mat[i][n - i - 1]; // add elements from secondary diagonal
        }
        if (n % 2 == 1) {
            int mid = n / 2;
            sum -= mat[mid][mid]; // remove the double-counted element at the center
        }
        return sum;
    }
}
