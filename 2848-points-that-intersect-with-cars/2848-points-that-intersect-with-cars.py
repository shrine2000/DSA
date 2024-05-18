class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        arr = [0] * 101 
        for num in nums:
            for i in range(num[0], num[1] + 1):
                arr[i] = 1  
        count = sum(arr)
        return count