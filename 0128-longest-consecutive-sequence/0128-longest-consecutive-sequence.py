class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 1
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                current_length = 1
                current_num = num
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                longest = max(current_length, longest)
        return longest