class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        count = 1
        
        dp[0] = 1
        
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1
            
            count += dp[i]
        
        return count
