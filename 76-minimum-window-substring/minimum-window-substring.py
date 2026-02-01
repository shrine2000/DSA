class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        char_map = [0] * 128
        count = len(t)
        start, end = 0, 0
        min_len = float("inf")
        start_idx = 0

        for char in t:
            char_map[ord(char)] += 1

        while end < len(s):
            if char_map[ord(s[end])] > 0:
                count -= 1

            char_map[ord(s[end])] -= 1
            end += 1

            while count == 0:
                if end - start < min_len:
                    min_len = end - start
                    start_idx = start

                if char_map[ord(s[start])] == 0:
                    count += 1
                char_map[ord(s[start])] += 1
                start += 1
        return "" if min_len == float("inf") else s[start_idx : start_idx + min_len]
