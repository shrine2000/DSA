class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack, result = [], [-1] * n
        for i in range(2 * n - 1, -1, -1):
            current_num = nums[i % n]
            while stack and stack[-1] <= current_num:
                stack.pop()
            if stack:
                result[i % n] = stack[-1]
            stack.append(current_num)
        return result