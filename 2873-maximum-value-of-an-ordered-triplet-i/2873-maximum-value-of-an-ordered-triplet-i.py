class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        m = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n): 
                    if i < j < k:
                        t = (nums[i] - nums[j]) * nums[k]
                        m = max(m, t)
                        
        return m