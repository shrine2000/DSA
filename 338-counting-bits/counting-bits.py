class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            ones_count = bin(i).count("1")
            res.append(ones_count)
        return res
