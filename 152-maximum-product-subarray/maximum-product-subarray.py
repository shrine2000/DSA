class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        @cache
        def dfs(i):
            if i == 0:
                return nums[0], nums[0]

            prev_max, prev_min = dfs(i - 1)

            num = nums[i]
            curr_max = max(num, num * prev_max, num * prev_min)

            curr_min = min(num, num * prev_max, num * prev_min)

            return  curr_max,curr_min

        answer = float("-inf")

        for i in range(len(nums)):
            curr_max, _ = dfs(i)
            answer = max(answer, curr_max)
        return answer
