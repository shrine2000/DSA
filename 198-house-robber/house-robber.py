class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        @cache
        def dfs(i):
            if i >= n:
                return 0
            pick = nums[i] + dfs(i + 2)
            not_pick = dfs(i + 1) 
            return max(pick, not_pick)
        ans = dfs(0)
        return ans
