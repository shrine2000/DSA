class Solution:
    def checkValidString(self, s: str) -> bool:
        low, high = 0, 0

        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            elif char == '*':
                low -= 1
                high += 1
            low = max(low, 0)
            if high < 0:
                return False
        return low == 0
