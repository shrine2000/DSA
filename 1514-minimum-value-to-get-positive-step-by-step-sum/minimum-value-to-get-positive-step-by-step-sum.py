class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        start_value = 1

        while True:
            is_valid = True
            curr = start_value

            for num in nums:
                curr += num
                if curr < 1:
                    is_valid = False
                    break
            if is_valid:
                return start_value
            start_value += 1
