class Solution:
    
    # Brute Force
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        n = len(merged)
        
        if n % 2 == 0:
            mid1 = merged[n // 2 - 1]
            mid2 = merged[n // 2]
            return (mid1 + mid2) / 2
        else:
            return merged[n // 2]