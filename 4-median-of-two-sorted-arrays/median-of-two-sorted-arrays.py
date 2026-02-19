class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_arr = sorted(nums1 + nums2)

        n = len(sorted_arr)
        mid = n // 2

        if n % 2 == 1:
            return sorted_arr[mid]
        else:
            return (sorted_arr[mid - 1] + sorted_arr[mid]) / 2
