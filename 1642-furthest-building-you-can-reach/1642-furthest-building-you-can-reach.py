class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        def check_reachability(heights, bricks, ladders, mid):
            diff = []  # Store height differences greater than previous ones
            
            # Calculate and store height differences for the first 'mid' buildings
            for i in range(1, mid + 1):
                if heights[i] > heights[i - 1]:
                    diff.append(heights[i] - heights[i - 1])
            
            # Sort the height differences in decreasing order
            # The largest differences can be covered using ladders
            diff.sort(reverse=True)
            
            l = len(diff)
            for i in range(ladders, l):
                if diff[i] > bricks:
                    return False  # Check if remaining differences can be covered using bricks
                bricks -= diff[i]
            return True
        
        n = len(heights)
        lo, hi = 0, n - 1
        
        # Binary search on the answer (furthest building index)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check_reachability(heights, bricks, ladders, mid):
                lo = mid  # If true, binary search on the right half
            else:
                hi = mid - 1  # If false, binary search on the left half
        
        return lo  # Return the index of the furthest reachable building
