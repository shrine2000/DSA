class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_profit = float("-inf")
        current_sum = 0
        for num in nums:
            current_sum = max(num + current_sum, num)
            max_profit = max(max_profit, current_sum)
        return max_profit
