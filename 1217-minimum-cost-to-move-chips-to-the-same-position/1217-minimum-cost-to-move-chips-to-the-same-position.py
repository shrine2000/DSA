class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd, even = 0, 0
        for p in position:
            if p % 2 == 0:
                even += 1
            else:
                odd += 1

        if even == 0 or odd == 0:
            return 0
        else:
            return min(even, odd)
