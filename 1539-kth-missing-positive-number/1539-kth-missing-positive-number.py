class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2
            missing_number = arr[mid] - (mid + 1)

            if missing_number < k:
                left = mid + 1
            else:
                right = mid - 1

        return k + left
