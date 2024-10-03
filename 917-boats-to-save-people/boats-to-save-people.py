class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:        
        boat = 0
        n = len(people)
        people.sort()

        i, j = 0, len(people) - 1
        while i <= j:
            s = people[i] + people[j]
            if s <= limit:
                boat += 1
                i += 1
                j -= 1
            else:
                boat += 1
                j -= 1
        return boat
                
            