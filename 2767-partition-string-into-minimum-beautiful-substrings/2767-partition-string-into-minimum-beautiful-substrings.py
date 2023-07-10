class Solution:
    def checkPower(self, x) -> bool:
        if x == 0:
            return False
        while x % 5 == 0:
            x //= 5
        return x == 1

    def findMinimumBeautifulSubstrings(self, s, index, dp) -> int:
        if index == len(s):
            return 0
        if s[index] == '0':
            return 20

        if dp[index] != -1:
            return dp[index]

        minSubstrings = 20
        currentVal = 0

        for i in range(index, len(s)):
            currentVal = currentVal * 2 + int(s[i])
            if self.checkPower(currentVal):
                minSubstrings = min(minSubstrings, 1 + self.findMinimumBeautifulSubstrings(s, i + 1, dp))
        dp[index] = minSubstrings
        return minSubstrings

    def minimumBeautifulSubstrings(self, s: str) -> int:
        dp = [-1] * len(s)
        minSubstrings = self.findMinimumBeautifulSubstrings(s, 0, dp)
        if minSubstrings > len(s):
            return -1
        return minSubstrings
