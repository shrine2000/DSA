class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        dpMin = [-1] * n
        dpMax = [-1] * n
        dpMin[0] = nums[0]
        dpMax[0] = nums[0]

        for k in range(1, n):
            if nums[k] >= 0:
                dpMin[k] = min(nums[k], nums[k] * dpMin[k - 1])
                dpMax[k] = max(nums[k], nums[k] * dpMax[k - 1])
            else:
                dpMin[k] = min(nums[k], nums[k] * dpMax[k - 1])
                dpMax[k] = max(nums[k], nums[k] * dpMin[k - 1])
            
            ans = max(ans, dpMax[k])
            
        return ans
