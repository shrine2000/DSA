class Solution:
    # https://www.geeksforgeeks.org/find-n-distinct-integers-with-zero-sum/

    def sumZero(self, n: int) -> List[int]:
        out = []
        for i in range(1, n // 2 + 1):
            out.append(i)
            out.append(-i)

        if n % 2 == 1:
            out.append(0)

        return out
