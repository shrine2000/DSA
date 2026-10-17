class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 1

        for i in range(n):
            remainder = nums[i] % k
            total = 0

            for j in range(i, n):
                if nums[j] % k != remainder:
                    break

                total += nums[j]

                if (total - nums[j]) % k == 0:
                    ans = max(ans, j - i + 1)

        return ans