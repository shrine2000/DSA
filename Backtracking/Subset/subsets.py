from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        result: List[List[int]] = []

        def backtrack(idx: int, current_combination: List[int]) -> None:
            # Append a copy of current_combination
            result.append(current_combination[:])

            # Explore further subsets
            for i in range(idx, N):
                current_combination.append(nums[i])
                backtrack(i + 1, current_combination)
                current_combination.pop()

        backtrack(0, [])
        return result


def test_subsets() -> None:
    sol = Solution()

    input_nums = [1, 2]
    expected_output = [[], [1], [1, 2], [2]]

    actual_output = sol.subsets(input_nums)
    assert sorted(map(sorted, actual_output)) == sorted(
        map(sorted, expected_output)
    ), f"Test failed for input {input_nums}. Expected {expected_output}, got {actual_output}"


if __name__ == "__main__":
    test_subsets()
