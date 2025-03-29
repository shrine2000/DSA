class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        max_len = 0
        curr_len = 0
        l = len(nums)

        for num in arr:
            if num - 1 not in arr:
                curr_len = 1
                temp = num
                while temp + 1 in arr:
                    curr_len += 1
                    temp += 1
            max_len=max(max_len, curr_len)
        return max_len


