class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_map = defaultdict(list)
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1
            if num_map[num] >= 2:
                return True
        return False