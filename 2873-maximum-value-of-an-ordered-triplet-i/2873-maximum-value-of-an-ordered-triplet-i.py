class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        m = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n): 
                    m = max(m, (nums[i] - nums[j]) * nums[k])
        return m