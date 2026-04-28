class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: 0 if x % 2 == 0 else 1)
        return nums
