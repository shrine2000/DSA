class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for idx, num in enumerate(nums):
            count[num] = count.get(num, 0) + 1
            if count[num] >= 2: return True
        return False