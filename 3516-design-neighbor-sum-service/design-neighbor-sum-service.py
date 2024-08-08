class neighborSum:
    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.r = len(grid)
        self.c = len(grid[0])
        self.position_map = {}
        for i in range(self.r):
            for j in range(self.c):
                self.position_map[grid[i][j]] = (i, j)
    
    def is_valid(self, a: int, b: int) -> bool:
        return 0 <= a < self.r and 0 <= b < self.c
    
    def adjacentSum(self, value: int) -> int:
        if value not in self.position_map:
            return 0
        
        x, y = self.position_map[value]
        s = 0
        for m, n in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + m, y + n
            if self.is_valid(nx, ny):
                s += self.grid[nx][ny]
        return s
    
    def diagonalSum(self, value: int) -> int:
        if value not in self.position_map:
            return 0
        
        x, y = self.position_map[value]
        s = 0
        dia = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
        for m, n in dia:
            nx, ny = x + m, y + n
            if self.is_valid(nx, ny):
                s += self.grid[nx][ny]
        return s

