class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        prev = None
        count = 0
        max_len = 0
        
        for num in sorted(nums):
            if prev is None or num == prev + 1:
                count += 1
            else:
                count = 1
                
            max_len = max(max_len, count)
            prev = num
            
        return max_len