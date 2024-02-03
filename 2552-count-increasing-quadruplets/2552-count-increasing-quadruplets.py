class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        sorted_list = []
        for k in range(n - 2, 1, -1):
            bisect_index = bisect_left(sorted_list, nums[k + 1])
            sorted_list.insert(bisect_index, nums[k + 1])
            i = 1 if nums[0] < nums[k] else 0
            for j in range(1, k):
                if nums[j] > nums[k]:
                    if i > 0:
                        index = bisect_left(sorted_list, nums[j])
                        count += i * (len(sorted_list) - index)
                else:
                    i += 1
        return count
