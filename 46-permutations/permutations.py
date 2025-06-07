class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(n):
            x = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(x)
            res.extend(perms)
            nums.append(x)
        return res
