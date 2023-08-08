from typing import List

class Solution:
    def maxHistogram(self, heights):
        heights.append(0)
        n = len(heights)
        stack = []
        res = 0 
        i = 0
        
        while i < n:
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                res = max(res, heights[top] * (i if not stack else i - stack[-1] - 1))
        return res
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        r, c = len(matrix), len(matrix[0])
        area = 0
        
        height = [0] * c
        
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
                
            area = max(area, self.maxHistogram(height))
        
        
        return area