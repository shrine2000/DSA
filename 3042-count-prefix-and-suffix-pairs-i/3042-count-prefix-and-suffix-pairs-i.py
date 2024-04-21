from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            n, m = len(str1), len(str2)
            if n > m:
                return False
            return str2[:n] == str1 and str2[-n:] == str1

        count = 0
        n = len(words)

        for i in range(n):
            for j in range(i + 1, n):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1

        return count
