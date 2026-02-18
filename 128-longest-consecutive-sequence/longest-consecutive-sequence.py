class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0
        n = len(nums_set)

        for num in nums_set:
            if num - 1 not in nums_set:
                current = num
                count = 1
                while current + 1 in nums_set:
                    current += 1
                    count += 1
                max_count = max(count, max_count)
        return max_count

