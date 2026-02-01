class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a set(), left, right pointers, run while loop till
        # right is less than length of string
        # if s[right] is not in set(), increment right, with max(max_len right-left)
        # else remove s[left] and increment left
        seen = set()
        l, r = 0, 0
        max_len = 0

        n = len(s)

        while r < n:
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                max_len = max(max_len, r - l)
            else:
                seen.remove(s[l])
                l += 1

        return max_len
