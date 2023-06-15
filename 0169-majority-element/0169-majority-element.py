class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else :
                hashmap[num] = 1
        
        mx = 0
        
        for key, value in hashmap.items():
            if value > mx:
                mx = value
                majority_element = key
            
        return majority_element