class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        res = []
        
        def backtrack(idx, curr_combo):
            if len(curr_combo) == k and sum(curr_combo) == n:
                res.append(curr_combo.copy())
                return
            if idx > len(nums) - 1:
                return
            
            curr_combo.append(nums[idx])
            backtrack(idx + 1, curr_combo)
            curr_combo.pop()
            backtrack(idx + 1, curr_combo)
            
        backtrack(0, [])
        return res