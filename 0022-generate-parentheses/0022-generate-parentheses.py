class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s, o, c):
            if len(s) == 2 * n:
                res.append(s)
                return
            
            if o < n:
                backtrack(s + "(", o + 1, c)
                
            if c < o:
                backtrack(s + ")", o, c + 1)
                
        res = []
        backtrack("", 0, 0)
        return res
                
                