class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(i):
            if i == 0:
                return nums[0], nums[0]

            prev_max, prev_min = dfs(i - 1)
            candidates = (nums[i], nums[i] * prev_max, nums[i] * prev_min)
            return max(candidates), min(candidates)

        return max(dfs(i)[0] for i in range(n))
