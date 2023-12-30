class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c = 0
        for _s in s:
            if _s == '1':
                c += 1

        if c == 0:
            return ""

        res = []  

        for i in range(c - 1):
            res.append('1')  

        for i in range(c, len(s)):
            res.append('0')  
            
        res.append('1')

        return ''.join(res)