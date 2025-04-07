from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane_algo(arr):
            curr_sum = 0
            max_sum = float('-inf')

            for num in arr:
                curr_sum = max(num, curr_sum + num)   
                max_sum = max(max_sum, curr_sum)  
            
            return max_sum

        normal_sum = kadane_algo(nums)   
        arr_sum = sum(nums)  
        min_arr_sum = kadane_algo([-num for num in nums])  
        if normal_sum < 0:
            return normal_sum
        
        return max(normal_sum, arr_sum + min_arr_sum)

 