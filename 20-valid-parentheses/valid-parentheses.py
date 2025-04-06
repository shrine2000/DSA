class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        stack = []

        for bracket in s:
            if bracket in char_map:
                stack.append(bracket)
            elif stack and char_map.get(stack[-1]) == bracket:
                stack.pop()
            else:
                return False 

        return not bool(stack)