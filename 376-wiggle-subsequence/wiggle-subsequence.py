class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        prev = nums[0]
        count = 1
        dir = 0

        for curr in nums[1:]:
            if curr > prev and dir != 1:
                count += 1
                dir = 1
            elif curr < prev and dir != -1:
                count += 1
                dir = -1
            prev = curr
        return count
