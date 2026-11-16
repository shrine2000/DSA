class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        N = len(nums)
        l, r = 0, N - 1
        while l < r:
            m = l + (r - l + 1) // 2 # this most important part
            if nums[m] > nums[m - 1]:
                l = m 
            else:
                r = m - 1
        return l
