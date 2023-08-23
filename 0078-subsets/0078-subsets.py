class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def gen(idx, curr):
            if idx == len(nums):
                res.append(curr[:])
                return 
            
            gen(idx + 1, curr)
            
            curr.append(nums[idx])
            gen(idx + 1, curr)
            curr.pop()
            
        
        gen(0, [])
        
        return res
            
        
            
            