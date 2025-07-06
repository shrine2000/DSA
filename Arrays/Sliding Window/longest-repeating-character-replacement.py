"""

Use a sliding window [l, r] to scan the string.

Keep a count of the most frequent character in the window.

If the number of characters that need to be replaced (window_size - max_freq) is greater than k, shrink the window from the left.

Else, expand the window from the right and update max length.

https://leetcode.com/problems/longest-repeating-character-replacement/solutions/91285/sliding-window-similar-to-finding-longes-to9w/

"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_state = defaultdict(int)
        max_char_count = 0
        result = 0
        left = 0

        for right in range(len(s)):
            window_state[s[right]] += 1

            max_char_count = max(max_char_count, window_state[s[right]])
            while (right - left + 1) - max_char_count > k:
                window_state[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result
