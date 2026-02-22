class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        @cache
        def dfs(start):
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set:
                    if dfs(end):
                        return True
            return False

        return dfs(0)
