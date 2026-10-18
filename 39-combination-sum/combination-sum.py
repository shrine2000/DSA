class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        #candidates.sort()
        path = []
        n = len(candidates)
        def backtrack(end, remaining):
            if remaining == 0:
                result.append(path[:])
                return 

            if remaining < 0 or end >= n:
                return

            for i in range(end, n):
                path.append(candidates[i])
                backtrack(i, remaining-candidates[i])
                path.pop()
        backtrack(0, target)
        return result
        