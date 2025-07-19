"""

Use a sliding window [l, r] to scan the string.

Keep a count of the most frequent character in the window.

If the number of characters that need to be replaced (window_size - max_freq) is greater than k, shrink the window from the left.

Else, expand the window from the right and update max length.

https://leetcode.com/problems/longest-repeating-character-replacement/solutions/91285/sliding-window-similar-to-finding-longes-to9w/

"""

from collections import defaultdict
from collections import Counter


class Solution:
    def brute_force(self, s: str, k: int) -> int:
        n: int = len(s)
        max_length: int = 0

        # Check all substrings
        for start in range(n):
            freq_counter: dict[str, int] = Counter()

            for end in range(start, n):
                current_char: str = s[end]
                freq_counter[current_char] += 1

                # Most frequent character count in current window
                max_freq: int = max(freq_counter.values())

                window_size: int = end - start + 1
                replacements_needed: int = window_size - max_freq

                # Check if this window is valid
                if replacements_needed <= k:
                    max_length = max(max_length, window_size)

        return max_length

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


if __name__ == "__main__":
    print(Solution().brute_force("AABABBA", 1))
