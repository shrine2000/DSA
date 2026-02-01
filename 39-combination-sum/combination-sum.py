class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(idx, curr, remaining):
            if remaining == 0:
                res.append(curr.copy())
                return

            if idx >= len(candidates) or remaining < 0:
                return

            curr.append(candidates[idx])
            backtrack(idx, curr, remaining - candidates[idx])
            curr.pop()
            backtrack(idx + 1, curr, remaining)

        backtrack(0, [], target)
        return res
