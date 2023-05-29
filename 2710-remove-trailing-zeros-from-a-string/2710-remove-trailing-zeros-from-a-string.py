class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        index = 0
        for i in range(len(num) - 1, -1, -1):
            if num[i] == '0':
                index += 1
            else:
                break

        result = num[:len(num) - index]
        return result