class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        N = len(s)
        @cache
        def dfs(idx):
            if idx == N:
                return True
            for end in range(idx + 1, N + 1):
                if s[idx:end] in word_set and dfs(end):
                    return True
            return False

        return dfs(0)
