from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        result = ""
        word_set = set(words)

        for word in words:
            can_be_built = True
            for i in range(1, len(word) + 1):
                substr = word[:i]
                if substr not in word_set:
                    can_be_built = False
                    break

            if can_be_built:
                if len(word) > len(result):
                    result = word
                elif len(word) == len(result) and word < result:
                    result = word

        return result
