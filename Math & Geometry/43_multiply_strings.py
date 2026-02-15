from typing import List


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = ord(num1[i]) - ord(
                    "0"
                )  # integer_value = ASCII_of_digit - ASCII_of_0
                digit2 = ord(num2[j]) - ord("0")

                product = digit1 * digit2

                position_low = i + j + 1
                position_high = i + j

                total = (
                    product + result[position_low]
                )  # add this multiplication result to whatever is already stored at this digit position.

                result[position_low] = total % 10  # stores current carry
                result[position_high] += total // 10  # store current digit

        result_str = "".join(map(str, result))

        return result_str.lstrip("0")  # lstrip removes artificial leading zeros


if __name__ == "__main__":
    sol = Solution()

    num1 = "123"
    num2 = "456"

    result = sol.multiply(num1, num2)

    print(f"{num1} × {num2} = {result}")
