class MedianFinder:

    def __init__(self):
        self.lower_half = []
        self.upper_half = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower_half, -num)
        heapq.heappush(self.upper_half, -heapq.heappop(self.lower_half))

        if len(self.upper_half) > len(self.lower_half):
            heapq.heappush(self.lower_half, -heapq.heappop(self.upper_half))

    def findMedian(self) -> float:
        if len(self.lower_half) > len(self.upper_half):
            return float(-self.lower_half[0])
        return (-self.lower_half[0] + self.upper_half[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()