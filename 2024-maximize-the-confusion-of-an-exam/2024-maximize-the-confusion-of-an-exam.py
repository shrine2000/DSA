class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        t_c, f_c = 0, 0
        n = len(answerKey)
        l, r = 0, 0

        maxLen = float("-inf")

        while r < n:
            if answerKey[r] == "F":
                f_c += 1
            if answerKey[r] == "T":
                t_c += 1

            if f_c > k and t_c > k:
                while f_c > k and t_c > k:
                    if answerKey[l] == "F":
                        f_c -= 1
                    if answerKey[l] == "T":
                        t_c -= 1
                    l += 1

            if f_c <= k or t_c <= k:
                maxLen = max(maxLen, r - l + 1)

            r += 1

        return maxLen
