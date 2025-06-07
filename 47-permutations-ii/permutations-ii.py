class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, visited):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                visited[i] = True
                path.append(nums[i])
                backtrack(path, visited)
                path.pop()
                visited[i] = False

        nums.sort()
        result = []
        backtrack([], [False] * len(nums))
        return result
