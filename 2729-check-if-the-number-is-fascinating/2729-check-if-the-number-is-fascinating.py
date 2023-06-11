class Solution:
    def isFascinating(self, n: int) -> bool:
        original_digits = str(n)
        
        concatenated_digits = original_digits + str(2 * n) + str(3 * n)
    
        unique_digits = set(concatenated_digits)

        return len(unique_digits) == 9 == len(concatenated_digits) and '0' not in unique_digits
