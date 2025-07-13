class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = temperatures
        n = len(arr)
        result = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and arr[i] >= arr[stack[-1]]:
                stack.pop()
            
            if stack:
                result[i] = stack[-1] - i
            
            stack.append(i)

        return result