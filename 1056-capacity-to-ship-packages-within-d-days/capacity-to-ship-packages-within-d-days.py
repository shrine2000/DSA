class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def condition(weights, capacity, D):
            total_wgt = 0
            days = 1
            curr_wgt = 0
            for wgt in weights:
                if curr_wgt + wgt <= capacity:
                    curr_wgt += wgt
                else:
                    days += 1
                    curr_wgt = wgt
                    if days > D:
                        return False
            return True

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if condition(weights, mid, days):
                right = mid
            else:
                left = mid + 1

        return left
