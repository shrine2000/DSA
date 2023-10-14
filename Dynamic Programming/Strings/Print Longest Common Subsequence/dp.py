def longest_common_subsequence(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[n][m]
    lcs = [''] * lcs_length

    i, j = n, m
    index = lcs_length - 1

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs[index] = s1[i - 1]
            index -= 1
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(lcs)


if __name__ == "__main__":
    s1 = "abcde"
    s2 = "bdgek"
    res = longest_common_subsequence(s1, s2)
    print(res)  
