class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        l = len(original)
        if l != m * n:
            return []

        res = [[0] * n for _ in range(m)]

        for i in range(l):
            row = i // n
            col = i % n
            res[row][col] = original[i]

        return res
