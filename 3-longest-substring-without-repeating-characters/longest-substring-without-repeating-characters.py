class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_len = 1
        n = len(s)
        for i in range(n - 1):
            char_map = set()
            char_map.add(s[i])
            cur_len = 1

            while i < n - 1 and s[i + 1] not in char_map:
                char_map.add(s[i + 1])
                cur_len = len(char_map)
                i += 1
            max_len = max(max_len, cur_len)
        return max_len


        
        