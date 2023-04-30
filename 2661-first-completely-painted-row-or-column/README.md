<h2><a href="https://leetcode.com/problems/first-completely-painted-row-or-column/">2661. First Completely Painted Row or Column</a></h2><h3>Medium</h3><hr><div><p>You are given a <strong>0-indexed</strong> integer array <code>arr</code>, and an <code>m x n</code> integer <strong>matrix</strong> <code>mat</code>. <code>arr</code> and <code>mat</code> both contain <strong>all</strong> the integers in the range <code>[1, m * n]</code>.</p>

<p>Go through each index <code>i</code> in <code>arr</code> starting from index <code>0</code> and paint the cell in <code>mat</code> containing the integer <code>arr[i]</code>.</p>

<p>Return <em>the smallest index</em> <code>i</code> <em>at which either a row or a column will be completely painted in</em> <code>mat</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="image explanation for example 1"><img alt="image explanation for example 1" src="https://assets.leetcode.com/uploads/2023/01/18/grid1.jpg" style="width: 321px; height: 81px;">
<pre><strong>Input:</strong> arr = [1,3,4,2], mat = [[1,4],[2,3]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="image explanation for example 2" src="https://assets.leetcode.com/uploads/2023/01/18/grid2.jpg" style="width: 601px; height: 121px;">
<pre><strong>Input:</strong> arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The second column becomes fully painted at arr[3].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n = mat[i].length</code></li>
	<li><code>arr.length == m * n</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= arr[i], mat[r][c] &lt;= m * n</code></li>
	<li>All the integers of <code>arr</code> are <strong>unique</strong>.</li>
	<li>All the integers of <code>mat</code> are <strong>unique</strong>.</li>
</ul>
</div>


## Solution


```java

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


```
Detailed explanation of the code:


```java

class Solution {
    public int firstCompleteIndex(int[] arr, int[][] mat) {
        int rows = mat.length;
        int cols = mat[0].length;
```



The function `firstCompleteIndex` takes two parameters: an integer array `arr` and a 2D integer array `mat`. The goal is to go through each integer in `arr`, find its corresponding cell in `mat`, and paint it. The function should then return the smallest index `i` such that either a row or a column is completely painted in `mat`.

The first two lines of the function set the variables `rows` and `cols` to the number of rows and columns in `mat`, respectively. This is done to make the code more readable and avoid calling `mat.length` and `mat[0].length` multiple times later on.

```java

// Store the locations of all the integers in mat
        int[][] integerLocations = new int[rows * cols][2];
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                int integer = mat[i][j];
                integerLocations[integer-1][0] = i; // Row index
                integerLocations[integer-1][1] = j; // Column index
            }
        }
```



The next block of code creates a 2D array `integerLocations` that stores the row and column indices of each integer in `mat`. The array has dimensions `rows * cols` by 2, where each row corresponds to an integer and the first column is the row index while the second column is the column index.

The loop iterates through every element in `mat`, retrieves the integer value at that element, and stores its row and column indices in `integerLocations`. Note that we subtract 1 from the integer value because the range of integers in `mat` is from 1 to `rows * cols`, while the array indices are 0-indexed.

```java

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
```



The final block of code loops through each integer in `arr`, retrieves its corresponding row and column indices from `integerLocations`, and increments the counters `paintedInRow` and `paintedInCol` at the respective indices. These counters keep track of the number of painted cells in each row and column.

After each iteration, the code checks if the current row or column has been fully painted. If a row has been fully painted, its counter in `paintedInRow` will equal `cols`. If a column has been fully painted, its counter in `paintedInCol` will equal `rows`. If either of these conditions is met, the function returns the current index `i`.

If no row or column is fully painted after iterating through all the integers in `arr`, the function returns -1.
