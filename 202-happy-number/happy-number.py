class Solution:
    def isHappy(self, n: int) -> bool:
        def dfs(inp, seen):
            if inp == 1:
                return True
            if inp in seen:
                return False
            seen.add(inp)
            nums = str(inp)
            s = 0
            for num in nums:
                square = int(num) * int(num)
                s += square
            return dfs(s, seen)

        return bool(dfs(n, set()))
