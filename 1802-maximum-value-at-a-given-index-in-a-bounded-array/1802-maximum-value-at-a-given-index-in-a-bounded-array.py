class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n
        maxValue = 1
        left = index
        right = index
        while right - left + 1 <= maxSum:
            maxSum -= right - left + 1
            left = max(left - 1, 0)
            right = min(right + 1, n - 1)
            maxValue += 1
            if left == 0 and right == n - 1:
                maxValue += maxSum // n
                break
        return maxValue
