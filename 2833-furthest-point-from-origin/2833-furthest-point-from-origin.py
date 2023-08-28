class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        from collections import Counter
        
        
        count = Counter(moves)
        
        l = count['L']
        r = count['R']
        _ = count['_']
        
        if l > r:
            l += _
        else:
            r += _
                  
        return abs(l - r)
