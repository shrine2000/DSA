from collections import defaultdict
from typing import Dict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        freq = defaultdict(int)

        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            freq[s[right]] += 1
            max_freq = max(max_freq, freq[s[right]])

            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length