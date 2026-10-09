class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        # -4 - 1 - 1  0 1 2

        for i in range(n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                value = nums[left] + nums[right] + nums[i]
                if value == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right- 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif value > 0:
                    right -= 1
                else:
                    left += 1

        return res

                
