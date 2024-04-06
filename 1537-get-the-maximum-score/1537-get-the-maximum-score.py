class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        prevX, prevY = 0, 0 
        sum1, sum2 = 0, 0 
        i, j = 0, 0
        m, n = len(nums1), len(nums2)
        MOD = 10**9 + 7

        
        while (i < m and j < n):
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i+=1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j+=1
            else:
                sum1 = sum2 = max(nums1[i] + prevX, nums2[j] + prevY)
                i+=1
                j+=1
            prevX, prevY = sum1, sum2

        while i < m:
            sum1 += nums1[i]
            i+=1
        while j < n:
            sum2 += nums2[j]
            j+=1

        return max(sum1, sum2) % MOD
