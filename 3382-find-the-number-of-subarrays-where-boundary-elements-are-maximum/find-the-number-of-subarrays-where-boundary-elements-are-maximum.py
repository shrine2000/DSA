class Solution:
    def prev_greater(self, nums):
        n = len(nums)
        result = [-1] * n
        s = []
        for i in range(n-1, -1, -1):
            while s and nums[i] > nums[s[-1]]:
                result[s[-1]] = i
                s.pop()
            s.append(i)
        return result
        
    def binary_search(self, arr, target):
        l, h = 0, len(arr)
        while l < h:
            m = l + (h - l) // 2
            if arr[m] <= target:
                l = m + 1
            else:
                h = m
        return l
    
    def numberOfSubarrays(self, nums: List[int]) -> int:
        n, result = len(nums), 0
        pGreater = self.prev_greater(nums)
        idx = {}
        for i in range(n):
            if nums[i] not in idx:
                idx[nums[i]] = [i]   
            else:
                idx[nums[i]].append(i)
            result += len(idx[nums[i]]) - self.binary_search(idx[nums[i]], pGreater[i])
        return result
