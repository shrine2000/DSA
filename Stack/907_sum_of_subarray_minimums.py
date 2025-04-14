def sum_of_subarray_minimums(array: list[int]) -> int:
    MODULO = 10**9 + 7
    size = len(array)

    stack = []
    next_smaller_left = [0] * size
    next_smaller_right = [0] * size

    # Step 1: Compute Next Smaller to the Left (NSL)
    for current_index in range(size):
        while stack and array[stack[-1]] > array[current_index]:
            stack.pop()

        # If stack is empty, there is no smaller to the left
        next_smaller_left[current_index] = stack[-1] if stack else -1
        stack.append(current_index)

    # Clear stack for next computation
    stack.clear()

    # Step 2: Compute Next Smaller to the Right (NSR)
    for current_index in range(size - 1, -1, -1):
        while stack and array[stack[-1]] >= array[current_index]:
            stack.pop()

        # If stack is empty, no smaller to the right
        next_smaller_right[current_index] = stack[-1] if stack else size
        stack.append(current_index)

    # Step 3: Calculate the total sum of subarray minimums
    total_sum = 0

    for index in range(size):
        count_of_subarrays_with_current_min = (index - next_smaller_left[index]) * (
            next_smaller_right[index] - index
        )
        contribution = array[index] * count_of_subarrays_with_current_min
        total_sum = (total_sum + contribution) % MODULO

    return total_sum


# Driver code
if __name__ == "__main__":
    input_array = [3, 1, 2, 4]
    result = sum_of_subarray_minimums(input_array)
    print("Sum of subarray minimums:", result)  # Expected: 17
