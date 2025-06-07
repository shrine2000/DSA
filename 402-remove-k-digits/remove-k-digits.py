class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1

            if stack or digit != "0":
                stack.append(digit)
        if k > 0:
            stack = stack[:-k]

        return "".join(stack) or "0"
