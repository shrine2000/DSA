from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def dfs(r1, c1, r2, c2, memo):
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')

            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]

            if r2 == n - 1 and c2 == n - 1:
                return grid[r2][c2]

            cherries = 0
            if r1 == r2 and c1 == c2:
                cherries += grid[r1][c1]
            else:
                cherries += grid[r1][c1] + grid[r2][c2]

            cherries += max(
                dfs(r1 + 1, c1, r2 + 1, c2, memo),
                dfs(r1, c1 + 1, r2 + 1, c2, memo),
                dfs(r1 + 1, c1, r2, c2 + 1, memo),
                dfs(r1, c1 + 1, r2, c2 + 1, memo)
            )

            memo[(r1, c1, r2, c2)] = cherries
            return cherries

        n = len(grid)
        memo = {}  # Memoization dictionary to store computed results
        result = dfs(0, 0, 0, 0, memo)
        return max(0, result)

if __name__ == "__main__":
    # Example usage
    solution = Solution()
    grid = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
    print(solution.cherryPickup(grid))  # Output: 5
