class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return []

        N = len(digits)
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            s: str = ''.join(str(digit) for digit in digits)
            new_s = int(s) + 1
            return [ int(new) for new in str(new_s)]
