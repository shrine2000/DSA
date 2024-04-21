class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zero_count = 0
        n = len(nums)
        
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                zero_count += 1
            else:
                i += 1
        
        nums.extend([0] * zero_count)
            
        