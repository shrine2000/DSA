class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        modifed = sorted(set(nums))
        max_len = 1
        n = len(modifed)
        count=1
        for i in range(n - 1):
            if modifed[i] == modifed[i+1] - 1:
                count += 1
            else:
                count = 1              
            max_len=max(count, max_len)
        return max_len



