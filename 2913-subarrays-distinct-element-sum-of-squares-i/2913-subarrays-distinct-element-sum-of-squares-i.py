class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = []
        n = len(nums)
        for i in range(n):
            for j in range(i, n+1):
                ans.append(len(set(nums[i:j]))**2)
                
        return sum(ans)