class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(x, y):
            visited.add((x, y))
            for i, (nx, ny) in enumerate(stones):
                if (nx, ny) not in visited and (nx == x or ny == y):
                    dfs(nx, ny)

        visited = set()
        count = 0
        for x, y in stones:
            if (x, y) not in visited:
                dfs(x, y)
                count += 1
        return len(stones) - count
