def find_celebrity_brute_force(M):
    N = len(M)

    def is_celebrity(c):
        for j in range(N):
            if j != c and M[c][j] == 1:
                return False
        for i in range(N):
            if i != c and M[i][c] == 0:
                return False
        return True

    for person in range(N):
        if is_celebrity(person):
            return person

    return -1


MATRIX1 = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]
MATRIX2 = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 1, 0]]

print(find_celebrity_brute_force(MATRIX1))  # Output: 2
print(find_celebrity_brute_force(MATRIX2))  # Output: -1
