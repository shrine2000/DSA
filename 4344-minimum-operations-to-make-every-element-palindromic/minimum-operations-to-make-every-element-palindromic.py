ODD, EVEN = [], []
for i in range(1, 100000):
    s = str(i)
    for p in (int(s + s[::-1]), int(s + s[-2::-1])):
        if p % 2:
            ODD.append(p)
        else:
            EVEN.append(p)
ODD.sort()
EVEN.sort()

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        total = 0
        for num in nums:
            pals = ODD if num % 2 else EVEN
            left, right = 0, len(pals) - 1
            while left < right:
                mid = (left + right) // 2
                if pals[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            diff = abs(pals[left] - num)
            if left > 0:
                diff = min(diff, num - pals[left - 1])
            total += diff // 2

        return total