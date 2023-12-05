class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        q = deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    q.append((i, j))
                else:
                    matrix[i][j] = -1 
                    
        while q:
            x, y = q.popleft()
            for r, c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nX, nY = x + r, y + c
                if 0 <= nX < len(matrix) and 0 <= nY < len(matrix[0]) and matrix[nX][nY] == -1:
                    matrix[nX][nY] = matrix[x][y] + 1
                    q.append((nX, nY))
                    
        return matrix