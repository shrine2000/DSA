from collections import deque
from typing import List


class Solution:
    def nearest(self, grid: List[List[int]]) -> List[List[int]]:
        if not grid or not grid[0]:
            return []

        rows = len(grid)
        cols = len(grid[0])

        # Initialize distance grid with infinity and queue
        distance = [[float("inf")] * cols for _ in range(rows)]
        queue = deque()

        # Populate the queue with all cells that contain `1` and initialize their distances to 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    distance[r][c] = 0

        # Define directions for moving up, down, left, and right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Perform BFS
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    # If the new position has a larger distance, update it
                    if distance[nr][nc] > distance[r][c] + 1:
                        distance[nr][nc] = distance[r][c] + 1
                        queue.append((nr, nc))

        return distance


# {
# Driver Code Starts

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            a = list(map(int, input().split()))
            grid.append(a)
        obj = Solution()
        ans = obj.nearest(grid)
        for i in ans:
            for j in i:
                print(j, end=" ")
            print()

# } Driver Code Ends
