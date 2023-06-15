class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = 0
        right = 0
        consecutive_count = 0
        longest_length = 1

        while right < len(s) - 1 and left <= right:
            right += 1
            if s[right] == s[right - 1]:
                consecutive_count += 1
            while consecutive_count >= 2:
                left += 1
                if s[left] == s[left - 1]:
                    consecutive_count -= 1
            longest_length = max(longest_length, right - left + 1)

        return longest_length
