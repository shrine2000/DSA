# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f5b


import collections as cl


def calculate_difficulty(mid):
    result = 0
    for duration, count in sessions.items():
        if duration % mid == 0:
            result += (duration // mid - 1) * count
        else:
            result += (duration // mid) * count
    return result


t = int(input())

for case in range(t):
    N, K = list(map(int, input().split()))
    session_durations = list(map(int, input().split()))

    differences = [0] * (N - 1)

    for i in range(N - 1):
        differences[i] = session_durations[i + 1] - session_durations[i]

    sessions = cl.Counter(differences)

    left, right = 1, max(differences)
    while left < right:
        mid = left + (right - left) // 2
        if calculate_difficulty(mid) <= K:
            right = mid
        else:
            left = mid + 1

    print("Case #{}: {}".format(case + 1, left))
