from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        min_num = min(nums)
        operations = 0
        while min_num < k:
            if min_num in count:
                count[min_num] -= 1
                if count[min_num] == 0:
                    del count[min_num]
            min_num = min(count.keys()) if count else float("inf")
            operations += 1
        return operations
