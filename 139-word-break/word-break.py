class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_set = set(wordDict)
        n = len(s)
        
        dp = [False] * (n + 1)
        dp[n] = True

        for start in range(n - 1, -1, -1):
            for end in range(start + 1, n + 1):
                if s[start:end] in word_set and dp[end]:
                    dp[start] = True    
        return dp[0]
