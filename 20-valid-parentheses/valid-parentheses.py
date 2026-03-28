class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        cMap = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in cMap:
                if not stack or stack[-1] != cMap[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0


 
