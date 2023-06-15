class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        largest_sum = nums[0]
        
        for num in nums[1:]:
            if max_sum > 0:
                max_sum += num
            else:
                max_sum = num
                
            if max_sum > largest_sum:
                largest_sum = max_sum
                    
        return largest_sum
