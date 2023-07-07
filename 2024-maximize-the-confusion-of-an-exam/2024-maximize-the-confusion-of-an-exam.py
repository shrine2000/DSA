class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        trueCount = 0
        falseCount = 0
        n = len(answerKey)
        start = 0
        end = 0
        maxLength = float('-inf')

        while end < n:
            if answerKey[end] == 'F':
                falseCount += 1
            if answerKey[end] == 'T':
                trueCount += 1

            if falseCount > k and trueCount > k:
                while falseCount > k and trueCount > k:
                    if answerKey[start] == 'F':
                        falseCount -= 1
                    if answerKey[start] == 'T':
                        trueCount -= 1
                    start += 1

            if falseCount <= k or trueCount <= k:
                maxLength = max(maxLength, end - start + 1)

            end += 1

        return maxLength
