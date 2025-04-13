class Solution:
    def sumSubarrayMins(self, array: List[int]) -> int:
        MODULO = 10**9 + 7
        size = len(array)

        stack = []
        next_smaller_left = [0] * size
        next_smaller_right = [0] * size

        for current_index in range(size):
            while stack and array[stack[-1]] > array[current_index]:
                stack.pop()

            next_smaller_left[current_index] = stack[-1] if stack else -1
            stack.append(current_index)

        stack.clear()

        for current_index in range(size - 1, -1, -1):
            while stack and array[stack[-1]] >= array[current_index]:
                stack.pop()
            next_smaller_right[current_index] = stack[-1] if stack else size
            stack.append(current_index)

        total_sum = 0

        for index in range(size):
            count_of_subarrays_with_current_min = (
                (index - next_smaller_left[index]) *
                (next_smaller_right[index] - index)
            )
            contribution = array[index] * count_of_subarrays_with_current_min
            total_sum = (total_sum + contribution) % MODULO

        return total_sum


    
            