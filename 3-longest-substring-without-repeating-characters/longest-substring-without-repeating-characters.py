class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0, 0
        max_len = 0

        n = len(s)

        while r < n:
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                max_len = max(max_len, r - l)
            else:
                seen.remove(s[l])
                l += 1
        return max_len
