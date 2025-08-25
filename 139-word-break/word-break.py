class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        @cache
        def backtrack(start):
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set and backtrack(end):
                    return True
            return False
        return backtrack(0)