class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        c = Counter(nums)
        for k, v in c.items():
            if v > (n / 2):
                return k
        return -1