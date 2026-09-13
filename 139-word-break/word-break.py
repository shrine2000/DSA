class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)
        @cache
        def dfs(idx):
            if idx == n:
                return True
            for end in range(idx + 1, n + 1):
                if s[idx:end] in word_set and dfs(end):
                    return True
            return False

        return dfs(0)
