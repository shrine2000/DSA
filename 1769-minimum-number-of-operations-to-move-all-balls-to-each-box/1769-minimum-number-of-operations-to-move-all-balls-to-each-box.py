from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = [1 if box == "1" else 0 for box in boxes]
        distance = sum([i for i in range(len(boxes)) if boxes[i] == 1])
        left = boxes[0]
        right = sum(boxes) - boxes[0]
        result = []
        result.append(distance)
        for i in range(1, len(boxes)):
            distance += left
            distance -= right
            left += boxes[i]
            right -= boxes[i]
            result.append(distance)
        return result
