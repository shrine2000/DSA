class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        c1 = list(s1)
        c2 = list(s2)
        
        for i in range(2):
            j = i + 2
            if c1[i] == c2[j]:
                c1[i], c1[j] = c1[j], c1[i]
        
        return ''.join(c1) == s2
 