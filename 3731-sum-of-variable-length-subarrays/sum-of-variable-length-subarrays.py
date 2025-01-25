class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        total_sum = 0
        
        for i in range(n):
            start = max(0, i - nums[i]) 
            total_sum += prefix_sum[i + 1] - prefix_sum[start]
        
        return total_sum
