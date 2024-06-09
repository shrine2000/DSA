class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            if char.isdigit():
                while stack and stack[-1].isdigit():
                    stack.pop()
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
