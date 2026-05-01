class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        n = len(arr)

        for i in range(n):
            for j in range(i, n):
                if (j - i + 1) % 2 == 1:
                    res += sum(arr[i:j+1])

        return res