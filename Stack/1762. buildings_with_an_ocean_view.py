# https://leetcode.ca/2021-04-14-1762-Buildings-With-an-Ocean-View/


def findBuildings(nums):
    stack = []
    result = []
    max_height = 0
    for i in range(len(nums) - 1, -1, -1):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if not stack:
            result.append(i)
        stack.append(i)
        max_height = max(max_height, nums[i])
    if max_height == (sum(nums) / len(nums)):
        return [len(nums) - 1]
    result.reverse()
    return result if result else len(nums)


if __name__ == "__main__":
    heights1 = [4, 2, 3, 1]
    assert findBuildings(heights1) == [0, 2, 3], "Test case 1 failed"

    heights2 = [4, 3, 2, 1]
    assert findBuildings(heights2) == [0, 1, 2, 3], "Test case 2 failed"

    heights3 = [1, 3, 2, 4]
    assert findBuildings(heights3) == [3], "Test case 3 failed"

    heights4 = [2, 2, 2, 2]
    assert findBuildings(heights4) == [3], "Test case 4 failed"
