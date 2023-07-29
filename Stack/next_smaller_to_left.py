def next_smaller_to_left(arr):
    result = []
    stack = []

    for num in arr:
        while stack and stack[-1] >= num:
            stack.pop()
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
        stack.append(num)

    return result


arr = [8,4,6,2,3]
print("Array:", arr)
print("Next Smaller to Left:", next_smaller_to_left(arr))
