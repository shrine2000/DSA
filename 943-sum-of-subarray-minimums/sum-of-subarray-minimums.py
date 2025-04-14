from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MODULO = 10**9 + 7

        def nsr(arr):
            stack = []
            res = [n] * n
            for i in range(n - 1, -1, -1):
                while stack and arr[stack[-1]] > arr[i]: 
                    stack.pop()
                if stack:
                    res[i] = stack[-1]
                stack.append(i)
            return res

        def nsl(arr):
            stack = []
            res = [-1] * n
            for i in range(n):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                if stack:
                    res[i] = stack[-1]
                stack.append(i)
            return res

        left = nsl(arr)
        right = nsr(arr)

        total_sum = 0

        for i in range(n):
            left_count = i - left[i]
            right_count = right[i] - i

            contribution = arr[i] * left_count * right_count
            total_sum = (total_sum + contribution) % MODULO

        return total_sum