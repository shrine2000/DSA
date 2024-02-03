# https://takeuforward.org/data-structure/longest-increasing-subsequence-dp-41/


def find_lis_recursive(ind, prev_index):
    if ind == n:
        return 0

    not_take = find_lis_recursive(ind + 1, prev_index)

    take = 0
    if prev_index == -1 or arr[ind] > arr[prev_index]:
        take = 1 + find_lis_recursive(ind + 1, ind)

    return max(not_take, take)


if __name__ == "__main__":
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    n = len(arr)
    result = find_lis_recursive(0, -1)
    print("Length of Longest Increasing Subsequence (Recursive):", result)
