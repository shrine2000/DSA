class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        N = len(nums)

        def backtrack(idx, curr):
            solutions.append(curr[:])

            for i in range(idx, N):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(0, [])
        return solutions
