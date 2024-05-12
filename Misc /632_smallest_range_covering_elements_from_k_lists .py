from typing import List, Tuple, Dict


def smallest_range(nums: List[List[int]]) -> Tuple[int, int]:
    # Create a list to store flattened tuples of numbers and their corresponding sublist index
    flat_nums: List[Tuple[int, int]] = []

    # Flatten the input lists and store them in flat_nums with their sublist index
    for i, sublist in enumerate(nums):
        for num in sublist:
            flat_nums.append((num, i))

    # Sort the flattened list of numbers
    flat_nums.sort()

    # Initialize variables to store the smallest range and its start and end indices
    min_range_width = float("inf")
    min_range_start, min_range_end = -1, -1

    # Iterate through all possible start and end indices
    for start in range(len(flat_nums)):
        # Dictionary to keep track of how many numbers from each sublist are included in the current range
        num_count: Dict[int, int] = {i: 0 for i in range(len(nums))}

        # Expand the range from the current start index
        for end in range(start, len(flat_nums)):
            num, sublist_idx = flat_nums[end]
            num_count[sublist_idx] += 1

            # Check if all sublists have at least one number in the current range
            if all(count > 0 for count in num_count.values()):
                # Calculate the width of the current range
                width = flat_nums[end][0] - flat_nums[start][0]

                # Update the smallest range if the current range is smaller
                if width < min_range_width:
                    min_range_width = width
                    min_range_start, min_range_end = (
                        flat_nums[start][0],
                        flat_nums[end][0],
                    )

    # Return the start and end values of the smallest range found
    return min_range_start, min_range_end


if __name__ == "__main__":
    # Example usage:
    nums: List[List[int]] = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    print(smallest_range(nums))  # Output: (20, 24)
