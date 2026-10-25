class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        ans = 0
        run = 0

        for num in nums:
            if num >= minK and num <= maxK:
                run +=1
                ans += run
            else:
                run = 0
        return ans