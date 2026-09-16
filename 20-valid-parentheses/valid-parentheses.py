class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {
            ")":"(",
            "}": "{",
            "]":"["
        }

        stack = []
        

        for char in s:
            if stack and stack[-1] == char_map.get(char):
                stack.pop()
            else:
                stack.append(char)
        print(stack)

        return not stack