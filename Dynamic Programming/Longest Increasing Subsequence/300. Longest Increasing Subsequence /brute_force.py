from itertools import combinations


"""
The brute force approach for finding the Longest Increasing Subsequence (Longest Increasing Subsequence) involves generating all possible 
subsequences of the input array and checking if each subsequence forms an increasing sequence. It selects the 
longest increasing subsequence among all the generated subsequences. This method has exponential time complexity
(O(2^n)) and is inefficient for large arrays.

"""


def longest_increasing_subsequence_bruteforce(arr):
    n = len(arr)
    max_length = 0
    lis = []

    for r in range(1, n + 1):
        for subsequence in combinations(arr, r):
            subsequence = list(subsequence)
            increasing = True
            for i in range(1, r):
                if subsequence[i] <= subsequence[i - 1]:
                    increasing = False
                    break
            if increasing and len(subsequence) > max_length:
                max_length = len(subsequence)
                lis = subsequence

    return max_length, lis


if __name__ == "__main__":
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    length, lis = longest_increasing_subsequence_bruteforce(arr)
    print(f"Length of Longest Increasing Subsequence (Brute Force): {length}")
    print(f"Longest Increasing Subsequence: {lis}")
