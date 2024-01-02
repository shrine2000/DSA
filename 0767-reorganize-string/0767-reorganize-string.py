class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        char_freq = {}

        for c in s:
            char_freq[c] = char_freq.get(c, 0) + 1
            if 2 * char_freq[c] > (n + 1):
                return ""

        sorted_s = sorted(s, key=lambda c: (char_freq[c], c), reverse=True)

        res = ""
        j = ((n - 1) // 2) + 1

        for i in range((n - 1) // 2 + 1):
            res += sorted_s[i]
            if j < n:
                res += sorted_s[j]
            j += 1

        return res
