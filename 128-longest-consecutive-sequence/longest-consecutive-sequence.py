class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        max_len = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                count = 1
                current = num
                while current + 1 in nums_set:
                    count += 1
                    current += 1
                max_len = max(max_len, count)
        return max_len
