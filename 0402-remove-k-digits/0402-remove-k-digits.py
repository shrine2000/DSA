class Solution:
    
    def nearest_greater_left(self, arr, k):
        n = len(arr)
        result = [-1] * n  

        stack = []  
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()

            if stack:
                result[i] = arr[stack[-1]]

            stack.append(i)

        return result

    def removeKdigits(self, num: str, k: int) -> str:
        res = self.nearest_greater_left(num, k)
        out = []
        for i in range(len(num)):
            while out and k > 0 and out[-1] > num[i]:
                out.pop()
                k -= 1
            out.append(num[i])

        while k > 0:
            out.pop()
            k -= 1
            
        result = "".join(out).lstrip("0")

        if not result:
            return "0"

        return result
