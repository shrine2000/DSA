class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(0, n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            value = nums[i]
            left = i + 1
            right = n - 1

            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if val == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif val > 0:
                    right -= 1
                else:
                    left += 1


        return res
