class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        ans = -1

        for i in range(len(nums)):
            p = -1
            for j in range(i + 1, len(nums)):
                if (nums[j] - nums[j - 1]) != p * -1:
                    break
                else:
                    ans = max(ans, j - i + 1)
                    p *= -1

        return ans
