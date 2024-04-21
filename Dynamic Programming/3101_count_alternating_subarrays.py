from typing import List


def countAlternatingSubarrays(nums: List[int]) -> int:
    sub = 0
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums) + 1):
            _sub = nums[i:j]
            is_alternating = True
            for k in range(len(_sub) - 1):
                if _sub[k] == _sub[k + 1]:
                    is_alternating = False
                    break
            if is_alternating:
                sub += 1
    return sub


# Example usage
nums = [0, 1, 1, 1]
all_subarrays = countAlternatingSubarrays(nums)
print(all_subarrays)
