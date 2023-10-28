def maximalRectangle(matrix):
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    max_area = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "1":
                max_width = n - j
                max_height = m - i
                for h in range(1, max_height + 1):
                    for w in range(1, max_width + 1):
                        is_valid_rectangle = all(matrix[i + x][j + y] == "1" for x in range(h) for y in range(w))
                        if is_valid_rectangle:
                            max_area = max(max_area, h * w)
    return max_area


if __name__ == "__main__":
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    result = maximalRectangle(matrix)
    print("Maximum Rectangle Area:", result)