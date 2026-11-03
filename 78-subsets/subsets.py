class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []


        def backtrack(start, path):
            # 1. Base case: Is the current path a valid solution?
            #if is_valid_solution(path):
            res.append(path.copy())

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
