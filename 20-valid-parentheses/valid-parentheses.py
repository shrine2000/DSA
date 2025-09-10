class Solution:
    def isValid(self, s: str) -> bool:
        count_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in count_map:
                if stack and stack[-1] == count_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack

        
