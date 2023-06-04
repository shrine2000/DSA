class Solution:
    def minimizedStringLength(self, s: str) -> int:
        distn = set()
        
        for char in s:
            distn.add(char)
            
        return len(distn)
