class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        merged = []
        N = len(nums)
        i = 0
        while i < N:
            arr = str(nums[i]) + str(nums[i + 1])
            merged.append(int(arr))
            i+=2
        merged.sort()
        return merged[0]
