class Solution {
    public int[] rowAndMaximumOnes(int[][] matrix) {
      int[] answer = new int[]{0, 0};
        
        for (int i = 0; i < matrix.length; i++) {
            int count = 0;
            for (int j = 0; j < matrix[0].length; j++) {
                count += matrix[i][j];
            }
            
            if (count > answer[1]) {
                answer[0] = i;
                answer[1] = count;
            }
        }
        return answer;
    }
}