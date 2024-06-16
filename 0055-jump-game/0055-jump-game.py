
# https://leetcode.com/problems/jump-game/discuss/2375320/INTERVIEW-SCENARIO(recursion-memoization-dp-greedy)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mr = 0
        for i in range(len(nums)):
            if i > mr:
                return False
            mr = max(mr, i + nums[i])

        return mr >= len(nums) - 1
