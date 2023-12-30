from typing import List


class Solution:
    def maximumSumOfHeights(self, A: List[int]) -> int:
        n = len(A)

        def make(A):
            ans = [0]
            stack = []
            total = 0
            for i in range(n):
                width = 1
                while stack and A[i] <= A[stack[-1][0]]:
                    i0, w0 = stack.pop()
                    total -= A[i0] * w0
                    width += w0

                stack.append([i, width])
                total += A[i] * width
                ans.append(total)

            return ans

        left = make(A)
        right = make(A[::-1])[::-1]
        return max(left[i] + right[i] for i in range(n + 1))


if __name__ == '__main__':
    solution = Solution()

    maxHeights1 = [5, 3, 4, 1, 1]
    assert solution.maximumSumOfHeights(maxHeights1) == 13

    maxHeights2 = [6, 5, 3, 9, 2, 7]
    assert solution.maximumSumOfHeights(maxHeights2) == 22

    maxHeights3 = [3, 2, 5, 5, 2, 3]
    assert solution.maximumSumOfHeights(maxHeights3) == 18

    print("All test cases passed.")
