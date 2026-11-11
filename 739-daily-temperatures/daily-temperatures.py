class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []

        temp = temperatures

        n = len(temp)
        res = [0] * n

        for i in range(n - 1, -1, -1):
            while stack and temp[stack[-1]] <= temp[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res