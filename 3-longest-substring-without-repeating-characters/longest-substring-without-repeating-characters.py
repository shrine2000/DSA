class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_found = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in last_found and last_found[char] >= left:
                left = last_found[char] + 1
            last_found[char] = right
            max_len = max(max_len, right - left + 1)
        return max_len
