class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        next_arr = [-1] * len(nums)

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                stack_top = stack.pop()
                next_arr[stack_top] = nums[i]

            stack.append(i)

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                stack_top = stack.pop()
                next_arr[stack_top] = nums[i]

        return next_arr
