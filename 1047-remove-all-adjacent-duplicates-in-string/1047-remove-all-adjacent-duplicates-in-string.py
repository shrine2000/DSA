class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if len(stack) > 0 and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        
        return ''.join(stack)
