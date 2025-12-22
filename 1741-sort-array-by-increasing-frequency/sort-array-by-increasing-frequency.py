from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        def sort_key(x):
            return (freq[x], -x)

        nums.sort(key=sort_key)
        return nums

        