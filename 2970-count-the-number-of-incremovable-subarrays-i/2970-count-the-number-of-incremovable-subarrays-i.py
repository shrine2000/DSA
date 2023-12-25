class Solution:
    def incremovableSubarrayCount(self, nums):
        count = 0
        length = len(nums)

        for i in range(length):
            for j in range(i, length):
                sub_arr = nums[i:j + 1] 
                temp = nums[:]
                temp[i:j + 1] = [] 

                strictly_increasing = True
                for k in range(len(temp) - 1):
                    if temp[k] >= temp[k + 1]:
                        strictly_increasing = False
                        break

                if strictly_increasing:
                    count += 1

        return count
