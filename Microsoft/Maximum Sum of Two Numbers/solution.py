def get_digit_sum(num):
    """Returns the digit sum of a given number."""
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    return digit_sum

n = int(input())
a = list(map(int, input().split()))

digit_sum_dict = {}
max_sum = -1

for num in a:
    digit_sum = get_digit_sum(num)
    if digit_sum in digit_sum_dict:
        pair_sum = num + digit_sum_dict[digit_sum]
        max_sum = max(max_sum, pair_sum)
        digit_sum_dict[digit_sum] = max(digit_sum_dict[digit_sum], num)
    else:
        digit_sum_dict[digit_sum] = num

print(max_sum)
