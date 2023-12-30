class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_ones(num):
            count = 0
            while num:
                count += num & 1
                num >>= 1
            return count

        res = [count_ones(i) for i in range(n + 1)]
        return res
        