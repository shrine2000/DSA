class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left, right = 0, 0
        res, max_freq = 0, 0
        freq = defaultdict(int)

        for right in range(n):
            freq[s[right]] += 1
            max_freq = max(max_freq, freq[s[right]])
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            res = max(res, right- left + 1)
        return res

            