class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = [("", 0, 0)]
        while stack:
            current, open_count, closed_count = stack.pop()
            if len(current) == 2 * n:
                result.append(current)
                continue

            if open_count < n:
                stack.append((current + "(", open_count + 1, closed_count))

            if closed_count < open_count:
                stack.append((current + ")", open_count, closed_count + 1))

        
        return result
