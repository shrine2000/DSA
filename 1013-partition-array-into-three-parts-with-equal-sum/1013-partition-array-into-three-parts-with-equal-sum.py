class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return False

        target_sum = total_sum // 3
        sum1, sum2 = 0, 0

        for i in range(len(arr) - 1):
            sum1 += arr[i]
            if sum1 == target_sum:
                for j in range(i + 1, len(arr)):
                    sum2 += arr[j]
                    if sum2 == target_sum and j < len(arr) - 1:
                        return True

        return False
