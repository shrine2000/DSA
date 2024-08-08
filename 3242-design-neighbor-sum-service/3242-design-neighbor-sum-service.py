class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.r = len(self.grid)
        self.c = len(self.grid[0])
    
    def is_valid(self, a, b):
        return bool(0 <= a < self.r and 0 <= b < self.c)
    
    def adjacentSum(self, value: int) -> int:
        x, y = 0, 0
        s = 0
        for i in range(self.r):
            for j in range(self.c):
                if self.grid[i][j] == value:
                    for m, n in [(0, 1), (0, -1), (1, 0), (-1 , 0)]:
                        if self.is_valid(i + m, j + n):
                            s += self.grid[i + m][j + n]
        return s
                            
    def diagonalSum(self, value: int) -> int:
        dia = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
        x, y = 0, 0
        s = 0
        for i in range(self.r):
            for j in range(self.c):
                if self.grid[i][j] == value:
                    for m, n in dia:
                        if self.is_valid(i + m, j + n):
                            s += self.grid[i + m][j + n]
        return s
        


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)