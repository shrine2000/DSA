from typing import List


def next_smaller_to_left(arr: List[int]) -> List[int]:
    result = [-1] * len(arr)
    stack = []

    for i in range(len(arr) - 1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)

    return result


arr = [4, 5, 2, 10, 8]
print("Next smaller to the left:", next_smaller_to_left(arr))
