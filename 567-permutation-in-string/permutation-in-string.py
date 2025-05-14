class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)

        if n > m:
            return False

        s1_counts = Counter(s1)
        window_counts = Counter(s2[:n])

        if s1_counts == window_counts:
            return True

        for right in range(n, m):
            window_counts[s2[right]] += 1

            window_counts[s2[right - n]] -= 1

            if window_counts[s2[right - n]] == 0:
                del window_counts[s2[right - n]]

            if s1_counts == window_counts:
                return True

        return False
