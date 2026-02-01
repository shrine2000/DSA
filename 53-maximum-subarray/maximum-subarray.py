class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_till_now = float("-inf")

        for num in nums:
            curr_sum = max(num, curr_sum + num)
            max_till_now = max(max_till_now, curr_sum)
        return max_till_now if max_till_now != float("-inf") else -1
