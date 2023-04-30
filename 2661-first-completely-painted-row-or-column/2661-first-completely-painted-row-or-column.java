class Solution {
    public int firstCompleteIndex(int[] arr, int[][] mat) {
        int rows = mat.length;
        int cols = mat[0].length;
        
        // Store the locations of all the integers in mat
        int[][] integerLocations = new int[rows * cols][2];
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                int integer = mat[i][j];
                integerLocations[integer-1][0] = i; // Row index
                integerLocations[integer-1][1] = j; // Column index
            }
        }
        
        // Count the number of painted cells in each row and column
        int[] paintedInRow = new int[rows];
        int[] paintedInCol = new int[cols];
        for (int i = 0; i < arr.length; ++i) {
            int integer = arr[i];
            int[] location = integerLocations[integer-1];
            int row = location[0];
            int col = location[1];
            
            // Increment the count of painted cells in the current row and column
            paintedInRow[row]++;
            paintedInCol[col]++;
            
            // If any row or column is fully painted, return the current index
            if (paintedInRow[row] == cols || paintedInCol[col] == rows) {
                return i;
            }
        }
        
        // No row or column is fully painted
        return -1;
    }
}
