class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])
        answer = [row[:] for row in matrix]
        for j in range(cols):
            max_value = float("-inf")
            for i in range(rows):
                if matrix[i][j] == -1:
                    continue
                max_value = max(max_value, matrix[i][j])

            for i in range(rows):
                if matrix[i][j] == -1:
                    answer[i][j] = max_value

        return answer
