class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        ts = nums[0] + nums[1]
        
        for k in range(3, len(nums), 2):
            if nums[k] + nums[k - 1] != ts:
                return k // 2
        return len(nums) //2
        