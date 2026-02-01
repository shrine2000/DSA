class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lnz = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lnz], nums[i] = nums[i], nums[lnz]
                lnz += 1
