class Solution:
    def maximizeGreatness(self, nums):
        nums.sort()   
        ans = 0
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] < nums[j]:
                ans += 1
                i += 1
            j += 1
        return ans
