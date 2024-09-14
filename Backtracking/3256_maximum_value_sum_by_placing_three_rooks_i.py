# https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/


class Solution:
    def maximumValueSum(self, board):
        m, n = len(board), len(board[0])
        max_sum = float("-inf")

        def backtrack(placed_rooks, current_sum, row_used, col_used):
            nonlocal max_sum

            if len(placed_rooks) == 3:
                max_sum = max(max_sum, current_sum)
                return

            for i in range(m):
                if row_used[i]:
                    continue

                for j in range(n):
                    if col_used[j]:
                        continue

                    placed_rooks.append((i, j))
                    row_used[i] = True
                    col_used[j] = True
                    current_sum += board[i][j]

                    backtrack(placed_rooks, current_sum, row_used, col_used)

                    placed_rooks.pop()
                    row_used[i] = False
                    col_used[j] = False
                    current_sum -= board[i][j]

        backtrack([], 0, [False] * m, [False] * n)

        return max_sum


if __name__ == "__main__":
    board = [[-3, 1, 1, 1], [-3, 1, -3, 1], [-3, 2, 1, 1]]
    print(Solution().maximumValueSum(board))  # 4

    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().maximumValueSum(board))  # 15
