class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        n = len(prices)
        res = prices[:]  
        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:  
                j = stack.pop()
                res[j] = prices[j] - prices[i]  
            
            stack.append(i)  
        
        return res