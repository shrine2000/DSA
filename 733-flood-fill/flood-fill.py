class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        if not image or not image[0]:
            return [[]]

        R, C = len(image), len(image[0])

        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        queue = deque([(sr, sc)])
        old_color = image[sr][sc]
        image[sr][sc] = color
        if old_color == color:
            return image

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = dx + x, dy + y

                if 0 <= nx < R and 0 <= ny < C:
                    if image[nx][ny] == old_color:
                        image[nx][ny] = color
                        queue.append((nx, ny))

        return image
