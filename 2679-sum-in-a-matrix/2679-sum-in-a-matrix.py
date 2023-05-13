class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        rows = len(nums)
        cols = len(nums[0])
        score = 0
        
        while rows > 0 and cols > 0:
            # Find the maximum number in each row
            row_max = []
            for i in range(rows):
                row_max.append(max(nums[i]))
                nums[i].remove(row_max[-1])
                
                if len(nums[i]) == 0:
                    rows -= 1
            
            # Add the maximum number to the score
            score += max(row_max)
            cols -= 1
        
        return score
