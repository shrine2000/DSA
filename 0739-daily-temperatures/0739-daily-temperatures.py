class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        
        stack = []
        answer = [0] * len(temp)
        
        
        for i in range(len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                top = stack.pop()
                answer[top] = i - top
            stack.append(i)
            
        return answer
                
        