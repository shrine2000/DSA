class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {')': '(', '}': '{', ']':'['}

        stack = []

        for char in s:
            if char in char_map.values():
                stack.append(char)
            elif not stack or  stack[-1] != char_map[char]:
                return False
            elif stack:
                stack.pop()
        return not stack
