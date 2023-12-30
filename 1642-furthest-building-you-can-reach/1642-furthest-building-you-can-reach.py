import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxHeap = []  
        
        lastHeight = heights[0]
        for idx, height in enumerate(heights[1:]):
            dif = height - lastHeight
            if dif > 0:
                bricks -= dif
                if bricks < 0:
                    if ladders == 0:
                        return idx  
                    ladders -= 1
                    bricks -= heapq.heappushpop(maxHeap, -dif)  
                else:
                    heapq.heappush(maxHeap, -dif)  
            lastHeight = height
        
        return len(heights) - 1  
