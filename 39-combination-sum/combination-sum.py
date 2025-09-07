class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(idx, path, curr_sum):
            if curr_sum == target:
                res.append(path[:])
                return path

            if idx >= len(candidates) or curr_sum > target:
                return

            for i in range(idx, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, curr_sum + candidates[i])
                path.pop()
       
        backtrack(0, [], 0)
        return res

        

