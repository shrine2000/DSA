def next_smaller_to_right(arr):
    """
    Find the Next Smaller to Right (NSR) for each element in the array.
    """
    stack = []
    result = [None] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])

    return result


def next_smaller_to_left(arr):
    """
    Find the Next Smaller to Left (NSL) for each element in the array.
    """
    stack = []
    result = [None] * len(arr)

    for i in range(len(arr)):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])

    return result


def next_greater_to_right(arr):
    """
    Find the Next Greater to Right (NGR) for each element in the array.
    """
    stack = []
    result = [None] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])

    return result


def next_greater_to_left(arr):
    """
    Find the Next Greater to Left (NGL) for each element in the array.
    """
    stack = []
    result = [None] * len(arr)

    for i in range(len(arr)):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])

    return result


def test_algorithms():
    test_cases = [
        ([4, 2, 5, 1, 6], "Test Case 1"),
        ([1, 2, 3, 4, 5], "Test Case 2"),
        ([5, 4, 3, 2, 1], "Test Case 3"),
        ([3, 3, 3, 3, 3], "Test Case 4"),
        ([1, 5, 2, 10, 6], "Test Case 5"),
        ([10, 5, 11, 6, 20, 12], "Test Case 6"),
    ]

    for arr, name in test_cases:
        print(f"{name}:")
        print(f"Array: {arr}")
        print(f"NSR: {next_smaller_to_right(arr)}")
        print(f"NSL: {next_smaller_to_left(arr)}")
        print(f"NGR: {next_greater_to_right(arr)}")
        print(f"NGL: {next_greater_to_left(arr)}")
        print()


if __name__ == "__main__":
    test_algorithms()
