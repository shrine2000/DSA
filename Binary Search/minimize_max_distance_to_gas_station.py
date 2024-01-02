class Solution:
    def findSmallestMaxDist(self, stations, K):
        def isPossible(stations, dist, K):
            count = 0
            for i in range(len(stations) - 1):
                distance = stations[i + 1] - stations[i]
                count += distance // dist

            return count <= K

        left, right = 0, max(stations) - min(stations)

        while right - left > 1e-6:
            mid = left + (right - left) / 2.0

            if isPossible(stations, mid, K):
                right = mid
            else:
                left = mid

        return round(left, 2)


solution = Solution()

stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 9
smallest_max_dist = solution.findSmallestMaxDist(stations, K)
print(smallest_max_dist)
