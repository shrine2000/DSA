class Solution:
    def balancedStringSplit(self, s: str) -> int:
        lCount, rCount = 0, 0

        count = 0
        for char in s:
            if char == "L":
                lCount += 1
            elif char == "R":
                rCount += 1
            if lCount == rCount:
                count += 1
                lCount = 0
                rCount = 0

        return count
