class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, path):
            if len(path) == k and sum(path) == n:
                ans.append(path[:])
                return
            
            for num in range(start, 10):
                if sum(path) + num > n:
                    break
                path.append(num)
                backtrack(num + 1, path)
                path.pop()
        
        ans = []
        backtrack(1, [])
        return ans
