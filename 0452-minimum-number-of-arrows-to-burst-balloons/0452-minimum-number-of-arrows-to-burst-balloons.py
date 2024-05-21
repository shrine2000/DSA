class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        prev = points[0][1]
        ans = 1
        for point in points[1:]:
            if point[0] > prev:
                ans += 1
                prev = point[1]
                
        return ans