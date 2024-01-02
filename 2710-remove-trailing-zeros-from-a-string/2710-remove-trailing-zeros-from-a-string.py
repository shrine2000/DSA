class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        if num is None or num == "":
            return ""
        index = len(num) - 1
        while index >= 0 and num[index] == "0":
            index -= 1
        if index < 0:
            return "0"

        return num[: index + 1]
