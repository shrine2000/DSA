class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = sum(nums[:3])
        N = len(nums)
        for i in range(N - 2):
            left = i + 1
            right = N - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(closest - target):
                    closest = total
                if total == target:
                    return total
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return closest
