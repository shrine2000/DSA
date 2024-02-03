class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        mx = 0
        for i in range(len(nums)):
            nums[i] += k
            mx = max(mx, nums[i])

        count = [0] * (mx + k + 2)

        for num in nums:
            count[num - k] += 1
            count[num + k + 1] -= 1

        total = 0
        ans = 1

        for i in range(mx + k + 2):
            total += count[i]
            ans = max(ans, total)

        return ans
