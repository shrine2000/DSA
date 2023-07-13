class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        
        def evalaute(i, curr_sum):
            if i == len(nums):
                if curr_sum == target:
                    return 1
                else:
                    return 0
                
            if (i, curr_sum) in dp:
                return dp[(i, curr_sum)]
            
            count = evalaute(i + 1, curr_sum + nums[i]) + evalaute(i + 1, curr_sum - nums[i])
            dp[(i, curr_sum)] = count
            
            return count
        
        return evalaute(0, 0)