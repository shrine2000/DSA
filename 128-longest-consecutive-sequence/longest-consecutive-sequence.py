class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_length = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                current = num
                length = 1
                while current + 1 in num_set:
                    length += 1
                    current += 1
                max_length = max(max_length, length)
        return max_length
