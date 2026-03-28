class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtracking(start, remaining, path):
            if remaining == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                
                path.append(candidates[i])
                backtracking(i, remaining-candidates[i], path)
                path.pop()
        backtracking(0, target, [])
        return res