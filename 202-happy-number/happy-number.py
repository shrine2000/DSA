class Solution:
    def isHappy(self, n: int) -> bool:
        def dfs(inp,seen):
            if inp == 1:
                return True
            if inp in seen:
                return False
            seen.add(inp)
            s = sum(int(digit) ** 2 for digit in str(inp))
            return dfs(s, seen)
        return bool(dfs(n,set()))


