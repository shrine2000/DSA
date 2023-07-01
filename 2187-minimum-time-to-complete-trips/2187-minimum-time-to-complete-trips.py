class Solution:
    def minimumTime(self, time, totalTrips):
        low = 1
        high = 2**63 - 100000
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if self.valid(time, mid, totalTrips):
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def valid(self, time, t, totalTrips):
        temp = 0
        for x in time:
            temp += t // x
            if temp >= totalTrips:
                return True
        return temp >= totalTrips
