class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        required = Counter(t)

        left = 0
        right = 0
        formed = 0
        minLength = float("inf")
        startIndex = 0

        while right < len(s):
            if s[right] in required:
                required[s[right]] -= 1
                if required[s[right]] >= 0:
                    formed += 1

            while formed == len(t):
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    startIndex = left

                if s[left] in required:
                    required[s[left]] += 1
                    if required[s[left]] > 0:
                        formed -= 1

                left += 1

            right += 1

        if minLength == float("inf"):
            return ""

        return s[startIndex : startIndex + minLength]
