def can_see_persons_count(heights):
    n = len(heights)
    answer = [0] * n
    stack = []

    for i in range(n - 1, -1, -1):
        count = 0
        while stack and heights[i] > heights[stack[-1]]:
            stack.pop()
            count += 1
        if stack:
            count += 1
        answer[i] = count
        stack.append(i)

    return answer


if __name__ == "__main__":
    heights = [10, 6, 8, 5, 11, 9]
    result = can_see_persons_count(heights)
    print(result)  # [3, 1, 2, 1, 1, 0]
