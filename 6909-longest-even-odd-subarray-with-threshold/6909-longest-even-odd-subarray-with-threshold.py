class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        l, r = 0, 0
        res = 0
        
        while(r < len(nums)):
            x = l - r
            
            if x % 2 == nums[r] % 2 and nums[r] <= threshold:
                res = max(res, r-l+1)
            else:
                if nums[r] % 2 == 0 and nums[r] <= threshold:
                    l = r
                else:
                    l = r + 1
            r += 1 
        
        return res
        
        
      
        
    