class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        seen =set(nums)
        
        for i in range(2 ** n):
            c = bin(i)[2:].zfill(n)
            if c not in seen: 
                return c
        return ""
        
        