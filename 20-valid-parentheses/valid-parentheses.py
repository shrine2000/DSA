class Solution:
    def isValid(self, s: str) -> bool:
        
        char_map = { ")": "(", "}":"{", "]":"["}
        stack = []
        for value in s:
            if stack and stack[-1] == char_map.get(value):
                stack.pop()
            else:
                stack.append(value)
        return not stack
                