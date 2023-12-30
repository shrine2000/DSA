class Solution {
    fun minPathSum(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val memo = Array(m) { IntArray(n) { -1 } }

        fun helper(x: Int, y: Int): Int {
            if (x == m - 1 && y == n - 1) {
                return grid[x][y]
            }
            if (x == m - 1) {
                return grid[x][y] + helper(x, y + 1)
            }
            if (y == n - 1) {
                return grid[x][y] + helper(x + 1, y)
            }

            if (memo[x][y] != -1) {
                return memo[x][y]
            }

            val down = helper(x + 1, y)
            val right = helper(x, y + 1)

            memo[x][y] = minOf(down, right) + grid[x][y]
            return memo[x][y]
        }

        return helper(0, 0)
    }
}
