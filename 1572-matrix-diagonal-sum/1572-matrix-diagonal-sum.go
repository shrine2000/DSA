func diagonalSum(mat [][]int) int {
    sum := 0
    n := len(mat)
    for i := 0; i < n; i++ {
        sum += mat[i][i] // add elements from primary diagonal
        sum += mat[i][n - i - 1] // add elements from secondary diagonal
    }
    if n % 2 == 1 {
        mid := n / 2
        sum -= mat[mid][mid] // remove the double-counted element at the center
    }
    return sum
}
