class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        count = 0
        prev = None
        max_len = 0

        for num in sorted(nums_set):
            if prev is None or num == prev + 1:
                count += 1
            else:
                count = 1  
            max_len = max(max_len, count)
            prev = num  

        return max_len
