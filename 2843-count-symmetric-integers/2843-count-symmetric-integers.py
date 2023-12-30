class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c = 0
        for i in range(low, high + 1):  
            str_i = str(i)
            if len(str_i) % 2 == 0:  
                n = len(str_i) // 2
                if sum(int(digit) for digit in str_i[:n]) == sum(int(digit) for digit in str_i[n:]):
                    c += 1
        return c
