class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start, cur, remaining):
            if remaining == 0:
                res.append(cur[:])
                return
            if remaining < 0:
                return 
            
            for i in range(start, len(candidates)):
                cur_can = candidates[i]
                cur.append(cur_can)
                backtrack(i, cur, remaining - cur_can)
                cur.pop()



        backtrack(0, [], target)
        return res