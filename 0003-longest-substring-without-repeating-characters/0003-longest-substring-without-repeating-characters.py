class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        res = 0
        
        charMap = {}
        
        for i in range(len(s)):
            if s[i] in charMap and charMap[s[i]] >= start:
                start = charMap[s[i]] + 1
                
            charMap[s[i]] = i
            
            current_len = i - start + 1
            res = max(res, current_len)
            
        return res
        
    
        
        