from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for num_passengers, start, end in trips:
            events.append((start, num_passengers))  
            events.append((end, -num_passengers))   

 
        events.sort(key=lambda x: (x[0], x[1]))

        current_capacity = 0
        for location, passenger_change in events:
            current_capacity += passenger_change
            if current_capacity > capacity:
                return False   

        return True  
