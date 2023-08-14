class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladders_used = []
        n = len(heights)
        
        for i in range(n - 1):
            climb = heights[i+1] - heights[i]
            
            if climb <= 0:
                continue
                
            if len(ladders_used) < ladders:
                heapq.heappush(ladders_used, climb)
            elif ladders_used and ladders_used[0] < climb:
                ladder_height = heapq.heappop(ladders_used)
                bricks -= ladder_height
                
                heapq.heappush(ladders_used, climb)
                
            else:
                bricks -= climb
                
            if bricks < 0:
                return i
            
        return n - 1