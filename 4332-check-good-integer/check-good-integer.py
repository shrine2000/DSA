class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digit_arr = []
        while n > 0:
            digit_arr.append(n % 10)
            n //= 10
        digit_sum = sum(digit_arr)
        squareSum = sum([i * i for i in digit_arr])
        return bool(squareSum - digit_sum >= 50)
