class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        
        if m < n:
            return ""

        l, r = 0, 0
        nFreq = defaultdict(int)

        for char in t:
            nFreq[char] += 1

        total = len(nFreq)
        formed = 0
        min_len = float('inf')
        ans = (0, 0)

        window_counts = defaultdict(int)

        while r < len(s):
            char = s[r]
            window_counts[char] += 1

            if char in nFreq and window_counts[char] == nFreq[char]:
                formed += 1

            while l <= r and formed == total:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    ans = (l, r)

                left_char = s[l]
                window_counts[left_char] -= 1

                if left_char in nFreq and window_counts[left_char] < nFreq[left_char]:
                    formed -= 1

                l += 1

            r += 1

        l, r = ans
        return "" if min_len == float('inf') else s[l:r+1]
