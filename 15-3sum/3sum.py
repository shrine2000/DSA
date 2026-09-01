class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []


        for i in range(n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            if nums[i] > 0:
                break

            left, right = i + 1, n - 1

            while left < right:
                target = nums[left] + nums[i] + nums[right]

                if target < 0:
                    left += 1
                elif target > 0:
                    right -= 1

                else:
                    res.append([nums[left], nums[i], nums[right]])

                    left += 1
                    right -=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1


        return res


