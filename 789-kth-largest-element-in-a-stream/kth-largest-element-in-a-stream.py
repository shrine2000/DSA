
class KthLargest:



    def __init__(self, k: int, nums: List[int]):

        self.k = k

        self.nums = nums

        heapq.heapify(self.nums)

        while len(self.nums) > k:

            heapq.heappop(self.nums)



    def add(self, val: int) -> int:

        if len(self.nums) < self.k:

            heapq.heappush(self.nums, val)

        else:

            heapq.heappushpop(self.nums, val)

        

        return self.nums[0]