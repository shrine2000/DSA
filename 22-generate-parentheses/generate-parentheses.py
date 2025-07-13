class Solution:
    def generateParenthesis(self, n):
        result = []
        stack = [("", 0, 0)]

        while stack:
            current, open_count, close_count = stack.pop()

            if len(current) == 2 * n:
                result.append(current)
                continue

            if open_count < n:
                stack.append((current + "(", open_count + 1, close_count))
            if close_count < open_count:
                stack.append((current + ")", open_count, close_count + 1))

        return result
