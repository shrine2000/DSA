import sys


def matrix_chain_multiplication(arr, L, R):
    # If the range contains only one matrix, return 0 (base case).
    if L == R:
        return 0

    res = sys.maxsize

    # Iterate through all possible split points (k) in the given range.
    for k in range(L, R):
        # Calculate the cost of multiplying matrices in two subchains and adding the cost of the merge.
        temp = matrix_chain_multiplication(arr, L, k) + matrix_chain_multiplication(arr, k + 1, R) + arr[L - 1] * arr[k] * arr[R]

        # Update the result with the minimum cost.
        res = min(res, temp)

    return res


if __name__ == "__main__":
    matrices = [10, 30, 5, 60]  # Example matrix dimensions
    n = len(matrices)  # Number of matrices

    # Call the recursive function to find the minimum cost.
    min_cost = matrix_chain_multiplication(matrices, 1, n - 1)

    print("Minimum cost of matrix chain multiplication:", min_cost)
