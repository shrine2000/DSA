class Solution:
    def minRotations(self, s: str) -> int:
        rotations = 0
        current = 0

        for digit in s:
            target = int(digit)

            clockwise = abs(current - target)
            counterclockwise = 10 - clockwise

            rotations += min(clockwise, counterclockwise)

            current = target

        return rotations