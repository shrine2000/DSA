class Solution {
    public int firstCompleteIndex(int[] arr, int[][] mat) {
       int m = mat.length, n = mat[0].length;
        int[][] loc = new int[m * n][2];
        for(int i =0; i < m; i++){
            for(int j = 0; j< n; ++j){
                loc[mat[i][j]-1][0] = i;
                loc[mat[i][j]-1][1] = j;
            }
        }
        
        int[] r = new int[m];
        int[] c = new int[n];
        
        for(int x =0; x < arr.length; ++x){
            int[] currentLoc = loc[arr[x]-1];
            int i = currentLoc[0];
            int j = currentLoc[1];
            if(++r[i] == n || ++c[j] == m) return x;
        }
        
        return -1;
    }
}
