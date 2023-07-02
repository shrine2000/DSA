def findKthPositive(arr, k):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        missing_count = arr[mid] - (mid + 1)

        if missing_count < k:
            left = mid + 1
        else:
            right = mid - 1

    return left + k

arr = [2, 3, 4, 7, 11]
k = 5
result = findKthPositive(arr, k)
print(result)  