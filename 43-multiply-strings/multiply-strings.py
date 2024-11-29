class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convert(nums):
            convert = {
                "0": 0,
                "1": 1,
                "2": 2,
                "3": 3,
                "4": 4,
                "5": 5,
                "6": 6,
                "7": 7,
                "8": 8,
                "9": 9,
            }

            i = 1
            value = 0
            for num in nums[::-1]:
                value += convert[num] * i
                i *= 10
            return value

        res = convert(num1) * convert(num2)
        return str(res)
