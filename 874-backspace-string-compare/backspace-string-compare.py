class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        
        for i in s:
            if i != '#':
                stack.append(i)
            elif stack:
                stack.pop()
        
        s = "".join(stack)
        stack = []
        for i in t:
            if i != '#':
                stack.append(i)
            elif stack:
                stack.pop()
        
        t = "".join(stack)
        return s == t