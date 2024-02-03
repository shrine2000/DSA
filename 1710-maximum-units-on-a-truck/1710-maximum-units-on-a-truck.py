class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        arr = sorted(boxTypes, key=lambda x: x[1], reverse=True)

        total_units = 0
        boxes_added = 0

        """
        [5, 10] = 50
        [3, 9]  = 27
        [4, 7]  = 28
        [2, 5]  = 10
        
        """

        for box_count, unit_per_box in arr:
            boxes_to_add = min(truckSize - boxes_added, box_count)
            total_units += boxes_to_add * unit_per_box
            boxes_added += boxes_to_add
            if boxes_added == truckSize:
                break

        return total_units
