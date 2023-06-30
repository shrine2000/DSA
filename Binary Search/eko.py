# https://www.spoj.com/problems/EKO/

def maxSawbladeHeight(N, M, heights):
    left = 0
    right = max(heights)

    while left < right:
        mid = (left + right + 1) // 2

        wood_cut = 0
        for height in heights:
            if height > mid:
                wood_cut += height - mid

        if wood_cut >= M:
            left = mid
        else:
            right = mid - 1

    return left


N, M = map(int, input().split())
heights = list(map(int, input().split()))
max_height = maxSawbladeHeight(N, M, heights)
print(max_height)
