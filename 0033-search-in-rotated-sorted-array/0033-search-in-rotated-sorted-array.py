class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for idx, value in enumerate(nums):
            if target == value:
                return idx
        return -1