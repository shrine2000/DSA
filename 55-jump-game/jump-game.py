class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_len = 0
        n = len(nums)
        for i in range(n):
            if i > max_len:
                return False
            max_len = max(max_len, i + nums[i])
            if max_len >= n - 1:
                return True

        return True
