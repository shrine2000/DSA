class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        # Map to store the last index of each character
        char_index_map: dict[str, int] = {}
        left = 0  # Left boundary of the window
        max_length = 0  # Result: max length of substring

        for right, char in enumerate(s):
            # If char is repeated and its last index is >= current window's start
            if char in char_index_map and char_index_map[char] >= left:
                # Move the left pointer right after the previous occurrence
                left = char_index_map[char] + 1

            # Update the last index of the current character
            char_index_map[char] = right
            # Update the max_length of the current window
            max_length = max(max_length, right - left + 1)

        return max_length


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
