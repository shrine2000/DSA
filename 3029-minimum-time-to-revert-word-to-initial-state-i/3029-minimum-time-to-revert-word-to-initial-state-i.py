class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        def z_function(s):
            n = len(s)
            z = [0] * n
            z[0] = n
            l = r = 0

            for i in range(1, n):
                if i <= r:
                    z[i] = min(z[i - l], r - i + 1)
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if z[i] > r - i + 1:
                    l, r = i, i + z[i] - 1

            return z

        n = len(word)
        z_values = z_function(word)

        for i in range(k, n, k):
            if z_values[i] == n - i:
                return i // k

        return (n + k - 1) // k
