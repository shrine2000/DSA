class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {')': '(', '}': '{', ']':'['}

        stack = []

        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif not stack or stack[-1] != char_map[char]:
                return False
            else:
                stack.pop()
        return not stack