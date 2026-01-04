class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c = Counter(s)

        for k, v in c.items():
            if not (v == next(iter(c.items()))[1]):
                return False
        return True
            
