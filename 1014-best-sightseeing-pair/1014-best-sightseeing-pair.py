class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = 0
        mx = A[0]

        for i in range(1, len(A)):
            mx = max(mx, A[i - 1] + (i - 1))
            res = max(res, A[i] - i + mx)

        return res
