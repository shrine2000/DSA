class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:         
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                nums = nums[i:] + nums[:i]
                if nums == sorted(nums):
                    return n - i
                else:
                    return -1
                
        return 0