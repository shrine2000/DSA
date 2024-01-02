class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n < 1:
            return 1

        if n >= 10:
            n = 10

        dp = [0] * (n + 1)
        dp[0] = 1

        #  combinatorial approach
        for i in range(1, n + 1):
            dp[i] = 9
            for j in range(9, 9 - i + 1, -1):
                dp[i] *= j

        return sum(dp)
