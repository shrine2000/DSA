from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        max_len = 1
        c = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                if nums[i] == nums[i - 1] + 1:
                    c += 1
                elif nums[i] != nums[i - 1]:
                    max_len = max(max_len, c)
                    c = 1

        return max(max_len, c)


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    nums_1 = [100, 4, 200, 1, 3, 2]
    expected_output_1 = 4
    assert (
        solution.longestConsecutive(nums_1) == expected_output_1
    ), "Test case 1 failed"

    nums_2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    expected_output_2 = 9
    assert (
        solution.longestConsecutive(nums_2) == expected_output_2
    ), "Test case 2 failed"

    print("All test cases passed!")
