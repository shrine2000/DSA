class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c = 0
        for i in range(low, high + 1):  
            s = str(i)
            if len(s) % 2 == 0 and sum(map(int, s[:len(s)//2])) == sum(map(int, s[len(s)//2:])):
                c += 1
        return c
