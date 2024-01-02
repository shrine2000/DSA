class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(index, target, candidates, ans, current_combination):
            if target == 0:
                ans.append(current_combination[:])
                return

            for i in range(index, len(candidates)):
                if candidates[i] > target:
                    break

                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                current_combination.append(candidates[i])
                backtrack(
                    i + 1, target - candidates[i], candidates, ans, current_combination
                )
                current_combination.pop()

        candidates.sort()
        ans = []
        current_combination = []
        backtrack(0, target, candidates, ans, current_combination)
        return ans
