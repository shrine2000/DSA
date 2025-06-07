class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        result: List[List[int]] = []

        def backtrack(idx, current_combination):
            result.append(current_combination[:])

            for i in range(idx, N):
                current_combination.append(nums[i])
                backtrack(i + 1, current_combination)
                current_combination.pop()

        backtrack(0, [])
        return result
