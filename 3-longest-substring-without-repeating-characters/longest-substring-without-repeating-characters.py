class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left, right, max_len = 0, 0, 0
        
        seen_chars = set()
        for right in range(n):
            while s[right] in seen_chars:
                seen_chars.remove(s[left])
                left += 1

                
            seen_chars.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len