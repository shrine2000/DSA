class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        p1, p2 = 0, 0

        while p1 < len(g) and p2 < len(s):
            if s[p2] >= g[p1]:
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        return p1
