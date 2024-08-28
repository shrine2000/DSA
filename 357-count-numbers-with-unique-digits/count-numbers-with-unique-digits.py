class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        ans = 10
        start = 9
        curr = 9
        while n > 1 and start:
            curr *= start
            start -= 1
            ans += curr
            n -= 1
        return ans