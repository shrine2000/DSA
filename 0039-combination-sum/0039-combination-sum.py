class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return
                
            if target < 0 or start >= len(candidates):
                return
            
            path.append(candidates[start])
            backtrack(start, target - candidates[start], path)
            path.pop()
            
            backtrack(start + 1, target, path)
            
        result = []
        backtrack(0, target, [])
        
        return result
            