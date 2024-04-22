class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count_c = 0
        total_substrings = 0

        for char in s:
            if char == c:
                count_c += 1
                total_substrings += count_c

        return total_substrings
