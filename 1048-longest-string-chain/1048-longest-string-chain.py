class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key=lambda x: len(x))

        longestChainLengths = [1] * n
        maxChainLength = 1

        def is_predecessor(prev, curr):
            M, N = len(prev), len(curr)

            if M >= N or N - M != 1:
                return False

            i, j = 0, 0

            while i < M and j < N:
                if prev[i] == curr[j]:
                    i += 1
                j += 1

            return i == M

        for i in range(n):
            for j in range(i):
                if is_predecessor(words[j], words[i]):
                    longestChainLengths[i] = max(
                        longestChainLengths[i], longestChainLengths[j] + 1
                    )
                    maxChainLength = max(maxChainLength, longestChainLengths[i])

        return maxChainLength
