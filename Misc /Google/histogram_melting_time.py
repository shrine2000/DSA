# https://leetcode.com/discuss/interview-question/125155/Google-or-Histogram-Melting-Time
# https://www.careercup.com/question?id=5650516169195520

"""
Given a histogram chart with values say {5,4,3,6,0,1}. Get the total count required to completely melt the histogram. A column with value 5 has 5 blocks in it. Any block which has air on any of its side gets melted.

Example 1:

Input: {5,4,3,6,0,1}
Output: 3
Expalantion: {5,4,3,6,0,1} -> {0,3,2,0,0} -> {0,0,0,0,0} => count=3
Example 2:

Input: {0,1,1,1,1,0}
Output: 2
Explanation: {0,1,1,1,1,0} -> {0,0,0,0,0} => count=2
"""


def melt_histogram(arr):
    count = 0
    while any(arr):
        melted = [0] * len(arr)
        for i in range(len(arr)):
            if i == 0 or i == len(arr) - 1:
                melted[i] = 0
            else:
                left = min(arr[i], arr[i - 1])
                right = min(arr[i], arr[i + 1])
                melted[i] = max(0, min(left, right, arr[i] - 1))
        arr = melted
        count += 1
    return count


if __name__ == "__main__":
    histogram1 = [5, 4, 3, 6, 0, 1]
    histogram2 = [0, 1, 1, 1, 1, 0]

    assert melt_histogram(histogram1) == 2  # Output: 2
    assert melt_histogram(histogram2) == 1  # Output: 1
