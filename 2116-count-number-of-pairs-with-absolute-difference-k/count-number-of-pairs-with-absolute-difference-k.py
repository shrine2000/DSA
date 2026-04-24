from collections import defaultdict

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(int)
        count = 0

        for num in nums:
            if (num - k) in hmap:
                count += hmap[num - k]
            if (num + k) in hmap:
                count += hmap[num + k]
            
            hmap[num] += 1
        
        return count