class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        N = len(digits)
        for i in reversed(range(N)):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + [0] * N
