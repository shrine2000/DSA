class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        values = {}

        result = []

        for num in nums:
            if num not in values:
                values[num] = True
                result.append(num)

        nums[:] = result

        return len(result)
