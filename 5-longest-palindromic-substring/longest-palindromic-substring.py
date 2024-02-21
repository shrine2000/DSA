class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _  in range(n)]
        
        start = 0
        max_l = 1
        
        for i in range(n):
            dp[i][i] = True
            
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_l = 2
                
        for l in range(3, n + 1):
            for i in range(n - l + 1):
                j = i + l  - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_l = l
                    
        return s[start:start + max_l]