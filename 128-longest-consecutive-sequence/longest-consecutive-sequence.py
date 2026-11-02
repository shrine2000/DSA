class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        count = 0
        for num in num_set:
            if num - 1 not in num_set:
                current = num
                c = 1
                while current + 1 in num_set:
                    current += 1
                    c += 1
                count = max(count, c)
        return count
