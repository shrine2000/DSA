class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max, max_till_now = 0, float('-inf')
        for num in nums:
            curr_max = max(num, curr_max + num)
            max_till_now = max(curr_max, max_till_now)
        return max_till_now

