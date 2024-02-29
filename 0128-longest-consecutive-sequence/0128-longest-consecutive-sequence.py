class Solution:
     def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hashset = set(nums)
        longestStreak = 0
        
        for num in nums:
            if num - 1 not in hashset:
                current_len = 1
                while num + 1 in hashset:
                    num += 1
                    current_len += 1
                    
                longestStreak = max(longestStreak, current_len)
                
        return longestStreak