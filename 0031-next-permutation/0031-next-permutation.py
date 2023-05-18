class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find the first decreasing element from the right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # If no decreasing element found, reverse the list
        if i == -1:
            nums.reverse()
            return
        
        # Find the next greater element than nums[i] from the right
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        
        # Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]
        
        # Reverse the elements after i
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1