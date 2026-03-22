class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        freq = defaultdict(int)
        best = 0
        l = 0

        for right in range(len(s)):
            freq[s[right]] += 1

            while freq[s[right]] > 1:
                freq[s[l]] -= 1
                l += 1

            best = max(best, right - l + 1)
        return best
