class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        stack = []
        count = 0
        prev_count = [0] * n
        
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] >= num:
                stack.pop()
                
            prev = stack[-1] if stack else -1
            prev_count[i] = prev_count[prev] + (i - prev) * num
            count += prev_count[i]
            stack.append(i)
        
        return count % MOD
