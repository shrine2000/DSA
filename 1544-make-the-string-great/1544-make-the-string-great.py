class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and stack[-1].isupper() and stack[-1].lower() == char:
                stack.pop()
            elif stack and stack[-1].islower() and stack[-1].upper() == char:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
