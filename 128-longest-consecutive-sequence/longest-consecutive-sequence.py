class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        maxlen = 1
        n = len(nums)
        l = 1
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                continue
                
            if nums[i + 1] - nums[i] == 1:
                l += 1
            else:
                l = 1
            maxlen = max(maxlen, l)
        return maxlen
    
 