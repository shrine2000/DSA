class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        out = []
        i = j = 0
        window_sum = 0

        while j < k and j < len(nums):
            window_sum += nums[j]
            out.append(-1)
            j += 1

        while j < len(nums):
            window_sum += nums[j]
            if j - i + 1 == 2 * k + 1:
                out.append(window_sum // (2 * k + 1))
                window_sum -= nums[i]
                j += 1
                i += 1

            elif j - i + 1 < 2 * k + 1:
                j += 1

        while len(out) != len(nums):
            out.append(-1)

        return out
