class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hmap = {}
        
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        
        return [k for k ,v in hmap.items() if v >= 2]