class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
      

        def backtrack(start, path, current_sum):
            if current_sum == target:
                result.append(path[:])
                return

            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, current_sum + candidates[i])
                path.pop()


        backtrack(0, [], 0)
        return result
