class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0
        nums3 = []
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1

        while i < n1:
            nums3.append(nums1[i])
            i += 1
        while j < n2:
            nums3.append(nums2[j])
            j += 1

        n3 = len(nums3)
        if n3 % 2 == 1:
            return nums3[n3 // 2]
        else:
            return (nums3[n3 // 2 - 1] + nums3[n3 // 2]) / 2
