


def matrix_chain_multiplication(arr, low, high):
    if low == high:
        return 0

    res = float('inf')

    for i in range(low, high):
        cost = matrix_chain_multiplication(arr, low, i) + matrix_chain_multiplication(arr, i + 1, high) + arr[low - 1] * arr[i] * arr[high]
        res = min(res, cost)

    return res


if __name__ == "__main__":
    matrices = [2, 4, 6, 8, 6]  # Example matrix dimensions
    n = len(matrices)  # Number of matrices

    # Call the recursive function to find the minimum cost.
    min_cost = matrix_chain_multiplication(matrices, 1, n - 1)

    print("Minimum cost of matrix chain multiplication:", min_cost)
