class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for i in range(1, n // 2 + 1):
            if n % i == 0:
                num_repeats = n // i
                substring = s[:i]
                if substring * num_repeats == s:
                    return True

        return False
