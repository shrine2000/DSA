class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        @lru_cache
        def recursion(total_step):
            if total_step == n:
                return 1
            if total_step > n:
                return 0
            return recursion(total_step + 1)+ recursion(total_step + 2)
        return recursion(0)