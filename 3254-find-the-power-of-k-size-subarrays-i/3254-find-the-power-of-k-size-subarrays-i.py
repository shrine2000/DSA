class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * (n - k + 1)

        for i in range(n - k + 1):
            subarray = nums[i : i + k]
            if self.is_consecutive_sorted(subarray):
                res[i] = max(subarray)
        return res

    def is_consecutive_sorted(self, arr: List[int]) -> bool:
        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1] + 1:
                return False
        return True
