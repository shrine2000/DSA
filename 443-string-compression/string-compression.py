class Solution:
    def compress(self, chars: list[str]) -> int:
        s = ""

        N = len(chars)

        low, high = 0, 0
        result = []

        while low <N:
            while high < N and chars[low] == chars[high]:
                high += 1

            count = high - low

            result.append(chars[low])

            if count > 1:
                result.extend(list(str(count)))

            low = high
        chars[:] = result
        return len(result)
