class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)

        @cache
        def dfs(idx, curr_sum):
            if curr_sum == target:
                return True

            if idx == n or curr_sum > target:
                return False

            return dfs(idx + 1, curr_sum + nums[idx]) or dfs(idx + 1, curr_sum)

        return dfs(0, 0)
