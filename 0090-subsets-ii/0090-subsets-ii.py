class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        self.backtracking(res,0,[],nums)
        return res
    def backtracking(self,res,start,subset,nums):
        res.append(list(subset))
        for i in range(start,len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            self.backtracking(res,i+1,subset,nums)
            subset.pop()