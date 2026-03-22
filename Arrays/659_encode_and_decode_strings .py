from typing import List


# https://www.lintcode.com/problem/659/
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    """
    @param: string: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, string: str) -> List[str]:
        res = []
        i = 0

        while i < len(string):
            j = i
            while string[j] != "#":
                j += 1

            length = int(string[i:j])
            j += 1

            word = string[j : j + length]
            res.append(word)

            i = j + length

        return res


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ["hello", "world"],
        ["", "a", ""],
        ["#hash", "123", "long_string_test"],
        [],
    ]

    for case in test_cases:
        encoded = sol.encode(case)
        decoded = sol.decode(encoded)

        print("Original:", case)
        print("Encoded :", encoded)
        print("Decoded :", decoded)
        print("Match   :", case == decoded)
        print("-" * 40)
