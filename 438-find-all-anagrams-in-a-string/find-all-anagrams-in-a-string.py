class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        len_p = len(p)
        len_s = len(s)
        left = 0

        target = Counter(p)
        window = Counter()
        result = []

        for right in range(len_s):
            window[s[right]] += 1

            while right - left + 1 > len(p):
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1

            if right - left + 1 == len(p):
                if window == target:
                    result.append(left)
        return result
