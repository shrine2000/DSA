class Solution:
    # Either rob houses from index 0 to n-2 (exclude last), OR from index 1 to n-1 (exclude first). Then take the max of both cases.
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
  
        def rob_linear(arr):
            prev2 = 0
            prev1 = 0

            for num in arr:
                curr = max(prev1, num + prev2)
                prev2 = prev1
                prev1 = curr
            return prev1
        if len(nums) == 1:
            return nums[0]
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
