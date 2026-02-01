class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        can = sorted(candidates)

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i == len(can):
                return
            curr.append(can[i])
            dfs(i + 1, curr, total + can[i])
            curr.pop()
            j = i
            while j + 1 < len(can) and can[j] == can[j + 1]:
                j += 1
            dfs(j + 1, curr, total)

        dfs(0, [], 0)
        return res
