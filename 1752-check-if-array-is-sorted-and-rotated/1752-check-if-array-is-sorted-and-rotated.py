class Solution:
    """
    This approach uses binary search to find the drop point, then checks if there is a decreasing sequence in the rotated array.

    """

    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                if nums[right - 1] > nums[right]:
                    left = right
                    break
                right -= 1

        smallest = left

        check = (smallest + 1) % n

        while check != smallest:
            if nums[check] < nums[check - 1]:
                return False
            check = (check + 1) % n

        return True
