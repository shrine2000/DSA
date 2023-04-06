class Solution {
     public int closedIsland(int[][] gd) {

            int m = gd.length;
            int n = gd[0].length;

            for (int i=0; i<m; i++) {
                dfs(gd, i, 0);
                dfs(gd, i, n-1);
            }

            for (int j=0; j<n; j++) {
                dfs(gd, 0, j);
                dfs(gd, m-1, j);
            }

            int isd = 0;
            for (int k=0; k<m; k++) {
                for (int l=0; l<n; l++) {
                    if (gd[k][l] == 0) {
                        isd++;
                        dfs(gd, k, l);
                    }
                }
            }

            return isd;
        }


        private void dfs (int[][] gd, int r, int c) {

            if (r < 0 || r > gd.length-1 || c <0 || c>gd[0].length-1 || gd[r][c] != 0) {
                return;
            }

            gd[r][c] = -1;

            dfs(gd, r+1, c);
            dfs(gd, r-1, c);
            dfs(gd, r, c+1);
            dfs(gd, r, c-1);

        }
}
