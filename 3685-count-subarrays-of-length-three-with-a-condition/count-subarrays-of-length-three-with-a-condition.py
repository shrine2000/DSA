class Solution:
    def _is_valid(self, nums):
        if not nums or len(nums) != 3:
            return False
        return bool(nums[1] / 2 == (nums[0] + nums[2]))

    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i, n):
                if self._is_valid(nums[i:j+1]):
                    count += 1
        return count

        