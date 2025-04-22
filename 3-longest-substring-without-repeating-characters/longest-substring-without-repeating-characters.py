class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_idx_map = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            if char in char_idx_map and char_idx_map[char] >= left:
                left = char_idx_map[char] + 1

            char_idx_map[char] = right
            max_length = max(max_length, right - left + 1)
        return max_length
