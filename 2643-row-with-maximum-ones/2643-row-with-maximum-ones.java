class Solution {
    public int[] rowAndMaximumOnes(int[][] mat) {
      int max_row = 0;
        int max_count = 0;
        
        for (int i = 0; i < mat.length; i++) {
            int oneCount = 0;
            for (int j = 0; j < mat[0].length; j++) {
                if (mat[i][j] == 1) {
                    oneCount++;
                }
            }
            if (oneCount > max_count) {
                max_count = oneCount;
                max_row = i;
            }
        }
        
        return new int[] {max_row, max_count};
    }
}