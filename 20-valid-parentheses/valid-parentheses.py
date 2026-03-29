class Solution:
    def isValid(self, s: str) -> bool:
        charMap = {")": "(", "}": "{", "]": "["}
        print(charMap.keys() )

        stack = []

        for char in s:
            if stack and char in charMap.keys() and charMap[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return not stack
