class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False] * 3

        for tpts in triplets:
            if tpts[0] > target[0] or tpts[1] > target[1] or tpts[2] > target[2]:
                continue
            
            for i in range(3):
                if tpts[i] == target[i]:
                    found[i] = True
        return all(found)
