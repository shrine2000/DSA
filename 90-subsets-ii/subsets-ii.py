class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        result: List[List[int]] = []

        def backtrack(idx, current_combination):
            result.append(current_combination[:])

            for i in range(idx, N):
                if i > idx and nums[i] == nums[i - 1]:
                    continue

                current_combination.append(nums[i])
                backtrack(i + 1, current_combination)
                current_combination.pop()

        nums.sort()
        backtrack(0, [])
        return result
