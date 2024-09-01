class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        """
        0, -5, -4, 1, 1, -6
        """
        m = 0
        max_altitude = 0
        for i in range(0, len(gain)):
            m += gain[i]
            max_altitude = max(max_altitude, m)
        return max_altitude
