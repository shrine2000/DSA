# O(N)


def generateSubarrays(nums):
    n = len(nums)
    result = []

    # Variables to keep track of subarray boundaries
    left = 0
    right = 0

    for right in range(n):
        # Calculate the number of subarrays that end at the current index
        # This is equivalent to the length of the subarray from 'left' to 'right'
        subarray_count = right - left + 1

        # Generate subarrays that end at the current index
        for i in range(subarray_count):
            subarray = nums[left + i : right + 1]
            result.append(subarray)

    return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    subarrays = generateSubarrays(nums)
    for subarray in subarrays:
        print(subarray)
