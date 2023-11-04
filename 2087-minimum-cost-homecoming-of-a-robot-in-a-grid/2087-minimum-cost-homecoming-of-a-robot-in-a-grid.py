from typing import List

class Solution:
    def minCost(self, s: List[int], h: List[int], r: List[int], c: List[int]) -> int:
        cost = 0

        for i in range(min(s[0], h[0]), max(s[0], h[0]) + 1):
            cost += r[i]

        for j in range(min(s[1], h[1]), max(s[1], h[1]) + 1):
            cost += c[j]

        cost -= (r[s[0]] + c[s[1]])

        return cost
