class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        char_set = set()

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            print(f"r - {r}, l - {l}, char_set - {list(char_set)}")
            max_len = max(max_len, r - l + 1)
        return max_len