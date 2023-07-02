class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i, n):
                if nums[j] > threshold:
                    break
                if (j - i) % 2 == 1 and nums[j] % 2 == 0:
                    break
                if (j - i) % 2 == 0 and nums[j] % 2 == 1:
                    break
                res = max(res, j - i + 1)
        return res
                    
        
        
      
        
    