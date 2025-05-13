class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m =len(nums1), len(nums2)
        nums3 = []
        i, j = 0, 0
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j+=1
            
        nums3.extend(nums1[i:])
        nums3.extend(nums2[j:])
        n = len(nums3)
        if n % 2 == 0:
            return (nums3[n // 2 - 1] + nums3[n // 2]) / 2
        else:
            return float(nums3[n // 2])