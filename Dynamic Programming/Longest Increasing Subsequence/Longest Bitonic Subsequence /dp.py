class Solution:
    def LongestBitonicSequence(self, nums):
        n = len(nums)

        # Initialize two DP arrays to store the lengths of increasing and decreasing subsequences.
        dp1 = [1] * n  # Increasing subsequence
        dp2 = [1] * n  # Decreasing subsequence

        # Compute the length of the longest increasing subsequence for each element in nums.
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp1[i] = max(dp1[i], 1 + dp1[j])

        # Compute the length of the longest decreasing subsequence for each element in nums.
        for i in range(n - 2, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[j] < nums[i]:
                    dp2[i] = max(dp2[i], 1 + dp2[j])

        # Initialize a variable to keep track of the maximum bitonic length.
        bitonic_length = 0

        # Calculate the length of the bitonic sequence for each element and find the maximum.
        for i in range(n):
            bitonic_length = max(bitonic_length, dp1[i] + dp2[i] - 1)

        return bitonic_length

