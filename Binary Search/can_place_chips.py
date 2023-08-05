#https://codeforces.com/problemset/problem/1809/B

def can_place_chips(n, s):
   return (s + 1) * (s + 1) >= n

def binary_search_minimum_cost(n):
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if can_place_chips(n, mid):
            right = mid
        else:
            left = mid + 1
    return left

t = int(input())

for _ in range(t):
    n = int(input())
    min_cost = binary_search_minimum_cost(n)
    print(min_cost)
