from typing import List
from collections import deque


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def bfs(start, target):
            visited = set()
            queue = deque([(start, 0)])
            visited.add(start)
            while queue:
                node, steps = queue.popleft()
                if node == target:
                    return steps
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x, y = node[0] + dx, node[1] + dy
                    if (
                        0 <= x < len(forest)
                        and 0 <= y < len(forest[0])
                        and (x, y) not in visited
                        and forest[x][y] != 0
                    ):
                        visited.add((x, y))
                        queue.append(((x, y), steps + 1))
            return -1

        trees = [
            (height, i, j)
            for i, row in enumerate(forest)
            for j, height in enumerate(row)
            if height > 1
        ]
        trees.sort()

        total_steps = 0

        current_position = (0, 0)
        for _, tx, ty in trees:
            target = (tx, ty)
            steps = bfs(current_position, target)
            if steps == -1:
                return -1
            total_steps += steps
            current_position = target
        return total_steps
