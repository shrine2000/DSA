class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def find_ans_for_prime(num):
            for ans in range(num):
                if ans | (ans + 1) == num:
                    return ans
            return -1
        
        return [find_ans_for_prime(num) for num in nums]
