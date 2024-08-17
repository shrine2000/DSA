from collections import deque
from typing import List


class Solution:
    @staticmethod
    def exist(matrix: List[List[str]], word: str) -> bool:
        if not matrix or not matrix[0]:
            return

        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols

        queue = deque([(0, 0)])
        visited = set()
        idx = 0
        if word[idx] == matrix[0][0]:
            visited.add((0, 0))
            idx += 1

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    is_valid(nx, ny)
                    and (nx, ny) not in visited
                    and matrix[nx][ny] == word[idx]
                ):
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    idx += 1

        return len(word) == idx


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    assert Solution.exist(matrix=board, word=word) == True
