class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n   
        pi, ni = 0, 1
        for num in nums:
            if num > 0:
                ans[pi] = num
                pi += 2
            else:
                ans[ni] = num
                ni += 2
            
        return ans
