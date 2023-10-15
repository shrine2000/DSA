class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        
        if n == 0:
            return 0
        
        elif self.isPalindrome(s):
            return 0
        
        reversed_s = s[::-1]
        
        lcs_length = self.longest_common_subsequence(s, reversed_s)
        
        min_insertions = n - lcs_length
        
        return min_insertions
    
    def isPalindrome(self, s) -> bool:
        return s == s[::-1]
    
    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]
