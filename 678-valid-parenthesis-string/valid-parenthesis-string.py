class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0
        max_open = 0

        for char in s:
            if char == "(":
                min_open += 1
                max_open += 1
            elif char == ")":
                min_open -=1
                max_open -=1
            else:
                min_open -= 1
                max_open += 1

            min_open = max(0, min_open)
            if max_open < 0:return False

        return min_open == 0
            