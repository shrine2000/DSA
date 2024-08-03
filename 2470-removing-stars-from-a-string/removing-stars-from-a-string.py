class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in range(n):
            if stack and s[i] == "*":
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
        