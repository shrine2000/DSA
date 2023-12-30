# https://atcoder.jp/contests/dp/tasks/dp_c


n = int(input())
a, b, c = [], [], []
for _ in range(n):
    i, j, k = map(int, input().split())
    a.append(i)
    b.append(j)
    c.append(k)

dpA = [0] * n
dpB = [0] * n
dpC = [0] * n

dpA[0] = a[0]
dpB[0] = b[0]
dpC[0] = c[0]

for i in range(1, n):
    dpA[i] = max(dpB[i - 1], dpC[i - 1]) + a[i]
    dpB[i] = max(dpA[i - 1], dpC[i - 1]) + b[i]
    dpC[i] = max(dpA[i - 1], dpB[i - 1]) + c[i]

print(max(dpA[-1], dpB[-1], dpC[-1]))
