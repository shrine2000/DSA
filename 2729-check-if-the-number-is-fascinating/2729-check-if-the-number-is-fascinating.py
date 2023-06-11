class Solution:
    def isFascinating(self, n: int) -> bool:
        new_digit = str(n) + str( 2 * n) + str(3 * n)
        unique_digits = set(new_digit)
        return len(unique_digits) == 9 and len(new_digit) ==  9 and '0' not in unique_digits