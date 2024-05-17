class Solution:
    def maximumPopulation(self, l: List[List[int]]) -> int:
        y = [0] * 101
        for b, d in l:
            y[b - 1950] += 1
            y[d - 1950] -= 1  
        p , c = 0, 0
        r = 0
        for i in range(101):
            c += y[i]
            if c > p:
                p = c
                r = i
        return r + 1950