class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)

        i = 0
        while i < n and s[i] == "a":
            i += 1

        if i == n:
            return s[: n - 1] + "z"

        result = list(s)
        for j in range(i, n):
            if s[j] != "a":
                result[j] = chr(ord(s[j]) - 1)
            else:
                break

        return "".join(result)
