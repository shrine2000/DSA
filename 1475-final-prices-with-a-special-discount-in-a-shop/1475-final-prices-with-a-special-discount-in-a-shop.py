from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        result = []
        stack = []

        for i in range(n - 1, -1, -1):  
            while stack and stack[-1] > prices[i]:
                stack.pop()
            if not stack:
                result.append(prices[i])  
            else:
                result.append(prices[i] - stack[-1])  
            stack.append(prices[i])

        return result[::-1]  

 