class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        def calculate(value, remaining):
            if remaining == 0:
                return int(value)
            new_num = 0
            for char in value:
                if char.isalpha():
                    num = ord(char) - ord("a") + 1
                    for digit in str(num):
                        new_num += int(digit)
                else:
                    new_num += int(char)
            return calculate(str(new_num), remaining - 1)
        return calculate(s, k)