class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0

        for start in range(n):
            for length in range(start + 1, n + 1):
                sub_string = s[start:length]
                count = {}

                for char in sub_string:
                    count[char] = count.get(char, 0) + 1

                valid = all(freq <= 2 for freq in count.values())

                if valid:
                    max_length = max(max_length, length - start)

        return max_length
